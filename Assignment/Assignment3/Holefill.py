from PIL import Image, ImageDraw
import numpy as np
import random
import os.path
import pickle

##############################################################################
#                        Functions for you to complete                       #
##############################################################################
# TODOPatch(Original image with black area)
# - TODOPatch size: [2 * patchL + 1, 2 * patchL + 1, 3]
# textureIm(Area on original image)
# - textureIm size: [texImRows, texImCols, 3]
# TODOMask
# - TODOMask: 1 is empty pixel, 0 is useful value. No 3rd dimension.
# - TODOMask size: [2 * patchL + 1, 2 * patchL + 1]
# ssdIm
# - ssdIm: is a result
# - ssdIm size: [texImRows - 2 * patchL, texImCols - 2 * patchL] because it takes care of boundary effect.

# Note: Convert TODOPatch and textureIm from uint8 to float32.


def ComputeSSD(TODOPatch: np.ndarray, TODOMask: np.ndarray, textureIm: np.ndarray, patchL: int) -> np.ndarray:
    patch_rows, patch_cols, patch_bands = np.shape(TODOPatch)
    tex_rows, tex_cols, tex_bands = np.shape(textureIm)
    ssd_rows = tex_rows - 2 * patchL
    ssd_cols = tex_cols - 2 * patchL
    SSD = np.zeros((ssd_rows, ssd_cols))

    # Step1: Iterate over SSD
    for resultSSDRow in range(ssd_rows):
        for resultSSDColumn in range(ssd_cols):
            # Step2: Iterate over patch
            for patchRow in range(patch_rows):
                for patchColumn in range(patch_cols):
                    # Step3: Check if it has valid pixel value, looking at TODOMask
                    if (TODOMask[patchRow, patchColumn] == 0):
                        # Step4: Find Row and Column in terms of original image input
                        universalRowAddress = resultSSDRow+patchRow
                        universalColumnAddress = resultSSDColumn+patchColumn
                        # Step5: Convert data type into float32
                        currentPatchPixel = TODOPatch[patchRow][patchColumn].astype(
                            np.float32)
                        currentTextureImPixel = textureIm[universalRowAddress][universalColumnAddress].astype(
                            np.float32)
                        # Step6: Calculate Sum Squared Difference
                        difference = currentPatchPixel-currentTextureImPixel
                        differenceSquared = difference**2
                        # Step7: Assign summation of calculated SSD from above, into corresponding pixel in SSD matrix
                        SSD[resultSSDRow][resultSSDColumn] += np.sum(
                            differenceSquared)
    return SSD

# The next section of Holefill.py takes the SSD image created above and
# chooses randomly amongst the best matching patches to decide which patch to paste into the texture image at that point.
# Next you need to write a functon CopyPatch which copies this selected patch into the final image.

# imHole: image with hole


def CopyPatch(imHole: np.ndarray, TODOMask: np.ndarray, textureIm: np.ndarray, iPatchCenter: np.int64, jPatchCenter: np.int64, iMatchCenter: np.int64, jMatchCenter: np.int64, patchL: int) -> np.ndarray:
    patchSize = 2 * patchL + 1

    for currentRowInPatch in range(patchSize):
        for currentColumnInPatch in range(patchSize):
            if (TODOMask[currentRowInPatch][currentColumnInPatch] == 1):
                # PatchCenter: center of the missing region on original image
                # Step1: Start from the top left corner of the missing region
                # Step1.1: Calculate row of the pixel that is going to be updated
                patchRow = (iPatchCenter-patchL)+currentRowInPatch
                # Step1.2: Calculate column of the pixel that is going to be updated
                patchColumn = (jPatchCenter-patchL)+currentColumnInPatch

                # MatchCenter: center of region that was selected, based on SSD samilarity
                # Step2: Start from the top left corner of the selected region
                # Step2.1: Calculate row of the pixel that is going to be updated
                textureRow = (iMatchCenter-patchL)+currentRowInPatch
                # Step2.2: Calculate column of the pixel that is going to be updated
                textureColumn = (jMatchCenter-patchL)+currentColumnInPatch

                # Step3: Update RGB pixel value for the missing region
                # Update Red channel
                imHole[patchRow][patchColumn][0] = textureIm[textureRow][textureColumn][0]
                # # Update Green channel
                imHole[patchRow][patchColumn][1] = textureIm[textureRow][textureColumn][1]
                # # Update Blue channel
                imHole[patchRow][patchColumn][2] = textureIm[textureRow][textureColumn][2]

    return imHole

##############################################################################
#                            Some helper functions                           #
##############################################################################


def DrawBox(im, x1, y1, x2, y2):
    draw = ImageDraw.Draw(im)
    draw.line((x1, y1, x1, y2), fill="white", width=1)
    draw.line((x1, y1, x2, y1), fill="white", width=1)
    draw.line((x2, y2, x1, y2), fill="white", width=1)
    draw.line((x2, y2, x2, y1), fill="white", width=1)
    del draw
    return im


def Find_Edge(hole_mask):
    [cols, rows] = np.shape(hole_mask)
    edge_mask = np.zeros(np.shape(hole_mask))
    for y in range(rows):
        for x in range(cols):
            if (hole_mask[x, y] == 1):
                if (hole_mask[x-1, y] == 0 or
                    hole_mask[x+1, y] == 0 or
                    hole_mask[x, y-1] == 0 or
                        hole_mask[x, y+1] == 0):
                    edge_mask[x, y] = 1
    return edge_mask

##############################################################################
#                           Main script starts here                          #
##############################################################################

#
# Constants
#


# Change patchL to change the patch size used (patch size is 2 *patchL + 1)
patchL = 10
patchSize = 2*patchL+1

# Standard deviation for random patch selection
randomPatchSD = 1

# Display results interactively
showResults = True

#
# Read input image
#

im = Image.open('donkey.jpg').convert('RGB')
im_array = np.asarray(im, dtype=np.uint8)
imRows, imCols, imBands = np.shape(im_array)

#
# Define hole and texture regions.  This will use files fill_region.pkl and
#   texture_region.pkl, if both exist, otherwise user has to select the regions.
if os.path.isfile('fill_region.pkl') and os.path.isfile('texture_region.pkl'):
    fill_region_file = open('fill_region.pkl', 'rb')
    fillRegion = pickle.load(fill_region_file)
    fill_region_file.close()

    texture_region_file = open('texture_region.pkl', 'rb')
    textureRegion = pickle.load(texture_region_file)
    texture_region_file.close()
else:
    # ask the user to define the regions
    print("Specify the fill and texture regions using polyselect.py")
    exit()

#
# Get coordinates for hole and texture regions
#

fill_indices = fillRegion.nonzero()
nFill = len(fill_indices[0])                # number of pixels to be filled
iFillMax = max(fill_indices[0])
iFillMin = min(fill_indices[0])
jFillMax = max(fill_indices[1])
jFillMin = min(fill_indices[1])
assert ((iFillMin >= patchL) and
        (iFillMax < imRows - patchL) and
        (jFillMin >= patchL) and
        (jFillMax < imCols - patchL)), "Hole is too close to edge of image for this patch size"

texture_indices = textureRegion.nonzero()
iTextureMax = max(texture_indices[0])
iTextureMin = min(texture_indices[0])
jTextureMax = max(texture_indices[1])
jTextureMin = min(texture_indices[1])
textureIm = im_array[iTextureMin:iTextureMax+1, jTextureMin:jTextureMax+1, :]
texImRows, texImCols, texImBands = np.shape(textureIm)
assert ((texImRows > patchSize) and
        (texImCols > patchSize)), "Texture image is smaller than patch size"

#
# Initialize imHole for texture synthesis (i.e., set fill pixels to 0)
#

imHole = im_array.copy()
imHole[fill_indices] = 0

#
# Is the user happy with fillRegion and textureIm?
#
if showResults == True:
    # original
    im.show()
    # convert to a PIL image, show fillRegion and draw a box around textureIm
    im1 = Image.fromarray(imHole).convert('RGB')
    im1 = DrawBox(im1, jTextureMin, iTextureMin, jTextureMax, iTextureMax)
    im1.show()
    print("Are you happy with this choice of fillRegion and textureIm?")
    Yes_or_No = False
    while not Yes_or_No:
        answer = input("Yes or No: ")
        if answer == "Yes" or answer == "No":
            Yes_or_No = True
    assert answer == "Yes", "You must be happy. Please try again."

#
# Perform the hole filling
#

while (nFill > 0):
    print("Number of pixels remaining = ", nFill)

    # Set TODORegion to pixels on the boundary of the current fillRegion
    TODORegion = Find_Edge(fillRegion)
    edge_pixels = TODORegion.nonzero()
    nTODO = len(edge_pixels[0])

    while (nTODO > 0):

        # Pick a random pixel from the TODORegion
        index = np.random.randint(0, nTODO)
        iPatchCenter = edge_pixels[0][index]
        jPatchCenter = edge_pixels[1][index]

        # Define the coordinates for the TODOPatch
        TODOPatch = imHole[iPatchCenter-patchL:iPatchCenter +
                           patchL+1, jPatchCenter-patchL:jPatchCenter+patchL+1, :]
        TODOMask = fillRegion[iPatchCenter-patchL:iPatchCenter +
                              patchL+1, jPatchCenter-patchL:jPatchCenter+patchL+1]

        #
        # Compute masked SSD of TODOPatch and textureIm
        #
        ssdIm = ComputeSSD(TODOPatch, TODOMask, textureIm, patchL)

        # Randomized selection of one of the best texture patches
        ssdIm1 = np.sort(np.copy(ssdIm), axis=None)
        ssdValue = ssdIm1[min(
            round(abs(random.gauss(0, randomPatchSD))), np.size(ssdIm1)-1)]
        ssdIndex = np.nonzero(ssdIm == ssdValue)
        iSelectCenter = ssdIndex[0][0]
        jSelectCenter = ssdIndex[1][0]

        # adjust i, j coordinates relative to textureIm
        iSelectCenter = iSelectCenter + patchL
        jSelectCenter = jSelectCenter + patchL
        selectPatch = textureIm[iSelectCenter-patchL:iSelectCenter +
                                patchL+1, jSelectCenter-patchL:jSelectCenter+patchL+1, :]

        #
        # Copy patch into hole
        #
        imHole = CopyPatch(imHole, TODOMask, textureIm, iPatchCenter,
                           jPatchCenter, iSelectCenter, jSelectCenter, patchL)

        # Update TODORegion and fillRegion by removing locations that overlapped the patch
        TODORegion[iPatchCenter-patchL:iPatchCenter+patchL +
                   1, jPatchCenter-patchL:jPatchCenter+patchL+1] = 0
        fillRegion[iPatchCenter-patchL:iPatchCenter+patchL +
                   1, jPatchCenter-patchL:jPatchCenter+patchL+1] = 0

        edge_pixels = TODORegion.nonzero()
        nTODO = len(edge_pixels[0])

    fill_indices = fillRegion.nonzero()
    nFill = len(fill_indices[0])

#
# Output results
#
if showResults == True:
    Image.fromarray(imHole).convert('RGB').show()
Image.fromarray(imHole).convert('RGB').save('results.jpg')

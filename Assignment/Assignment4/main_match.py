import hw_utils as utils
import matplotlib.pyplot as plt


def main():
    # Test run matching with no ransac
    plt.figure(figsize=(20, 20))
    im = utils.Match('./data/scene', './data/basmati', ratio_thres=0.63)
    plt.title('FindBestMatches(); threshold=0.63')
    plt.imshow(im)
    # save image as jpg
    plt.savefig('Q1-3.png')

    # Test run matching with ransac
    plt.figure(figsize=(20, 20))
    im = utils.MatchRANSAC(
        './data/library', './data/library2',
        ratio_thres=0.65, orient_agreement=45, scale_agreement=0.3)
    plt.title(
        'RANSACFilter(); ratio_threshold=0.65; orientation_agreement=45°; scale_agreement=30%')
    plt.imshow(im)
    plt.savefig('Q1-4.png')


if __name__ == '__main__':
    main()

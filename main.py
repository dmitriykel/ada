import utils
import config

if __name__ == "__main__":
    styled_img, img_loss = utils.run_style_transfer(config.SOURCE_IMG_PATH, config.STYLE_IMG_PATH, num_iterations=1)
    utils.save_img(styled_img, config.RESULT_IMG_PATH)



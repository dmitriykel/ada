from envparse import env

MAX_IMG_DIMENSIONAL = env.int("MAX_IMG_DIMENSIONAL", default=1024)
SOURCE_IMG_PATH = env.str("SOURCE_IMG_PATH", default="images/source/source.jpg")
STYLE_IMG_PATH = env.str("STYLE_IMG_PATH", default="images/style/style.jpg")
RESULT_IMG_PATH = env.str("RESULT_IMG_PATH", default="images/result/")
ITERATIONS_NUM = env.int("ITERATIONS_NUM", default=1000)
CONTENT_WEIGHT = env.float("CONTENT_WEIGHT", default=1e3)
STYLE_WEIGHT = env.float("STYLE_WEIGHT", default=1e-2)
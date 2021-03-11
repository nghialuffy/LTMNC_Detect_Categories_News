import pickle, os


REGULATE_PATH = "./models"
label_encode = ["công_nghệ", "du_lịch", "giáo_dục", "giải_trí", "kinh_doanh", "nhịp_sống", "phim_ảnh", "pháp_luật", "sống_trẻ", "sức_khỏe", "thế_giới", "thể_thao", "thời_sự", "thời_trang", "xe_360", "xuất_bản", "âm_nhạc", "ẩm_thực"]
nb_model = pickle.load(open(os.path.join(REGULATE_PATH, "linear_classifier.pkl"), 'rb'))
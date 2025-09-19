# Bài Tập Lớn Học Máy – CO3117 (Nhóm CEML2, Lớp TN01)

## Thông tin môn học
- **Tên môn học:** Học Máy  
- **Mã môn:** CO3117  
- **Lớp:** TN01 – Nhóm CEML2  
- **Học kỳ:** 251, Năm học 2025 – 2026  

## Giảng viên hướng dẫn
- **TS. Lê Thành Sách**

## Thành viên nhóm
- **Trương Thiên Ân** – 2310190 – an.truong241105@hcmut.edu.vn  
- **Lại Nguyễn Hoàng Hưng** – 2311327 – hung.lai2805@hcmut.edu.vn  
- **Nguyễn Tô Quốc Việt** – 2313898 – viet.nguyenluminous@hcmut.edu.vn  

---

## Mục tiêu bài tập lớn
 1. Hiểu và áp dụng được quy trình pipeline học máy truyền thống, bao gồm: tiền xử lý dữ liệu, trích xuất đặc trưng, huấn luyện và đánh giá mô hình.
 2. Rèn luyện kỹ năng triển khai mô hình học máy trên các loại dữ liệu khác nhau: bảng, văn bản, và ảnh.
 3. Phát triển khả năng phân tích, so sánh, và đánh giá hiệu quả của các mô hình học máy thông qua các chỉ số đo lường.
 4. Rèn luyện kỹ năng lập trình, thử nghiệm, và tổ chức báo cáo khoa học
 
## Assignment 1
### Mục tiêu bài tập
1. **Xử lý dữ liệu đầu vào**  
   - Thực hành xử lý giá trị thiếu (*missing values*) bằng kỹ thuật imputation.  
   - Thực hành mã hóa biến phân loại (*categorical features*) bằng kỹ thuật encoding.  

2. **Xây dựng pipeline học máy cho dữ liệu dạng bảng (Tabular Data)**  
   - Chuẩn hóa dữ liệu bằng các kỹ thuật impute và encoding.  
   - Lựa chọn và thực hiện giảm chiều dữ liệu bằng PCA (nếu cần).  
   - Áp dụng các mô hình học máy (ví dụ: Logistic Regression, SVM, Random Forest).  

3. **So sánh và đánh giá mô hình**  
   - So sánh hiệu quả giữa các mô hình đã huấn luyện.  
   - Đưa ra báo cáo kết quả: phân tích dữ liệu (EDA), mô tả pipeline, cấu hình các bước xử lý, và đánh giá.  

4. **Mở rộng (Extension)**  
   - Thử nghiệm hoặc tối ưu thêm (mô hình nâng cao, kỹ thuật ensemble, tuning hyperparameters, …).  

---

### Dataset
- **Tên:** *Mobile Phones in Indian Market Datasets*  
- **Nguồn:** [Kaggle Link](https://www.kaggle.com/datasets/kiiroisenkoxx/2025-mobile-phones-in-indian-market-datasets/data?select=mobiles_uncleaned.csv)  
- **Mô tả:** 11.786 mẫu, 14 thuộc tính về đặc điểm kỹ thuật và thông tin của các dòng điện thoại.  
- **Mục tiêu:** phân loại điện thoại theo giá (`low / medium / high`).  

**Cách tải dataset trong Colab:**  
Dataset đã được push lên GitHub, đã được cấu hình sẵn trong notebook để đảm bảo sẽ tự động tải sau khi nhấn Run Time -> Run all:
```bash
!wget https://raw.githubusercontent.com/HoangHungLN/MachineLearning_Assigment/refs/heads/main/data/mobiles_uncleaned.csv -O mobiles_uncleaned.csv
```
### Mô tả các module
- **`__init__.py`**:  
  Khai báo và gom tất cả hàm trong `feature_extractors.py` để tiện import (`extract_is_dual_sim`, `extract_cpu_speed`, `extract_ram`, ...).  

- **`feature_extractors.py`**:  
  Chứa các hàm *feature engineering* để trích xuất đặc trưng từ dữ liệu thô (chuỗi văn bản) thành dạng số:  
  - `extract_is_dual_sim`, `extract_is_5g`, `extract_is_nfc`  
  - `extract_cpu_brand`, `extract_cpu_speed`, `extract_cpu_core`  
  - `extract_ram`, `extract_rom`, `extract_battery`, `extract_fast_charging`  
  - `extract_screen_size`, `extract_refresh_rate`, `extract_ppi`  
  - `extract_rear`, `extract_front_camera`  
  - `extract_expandable_storage`, `extract_os`  

- **`model_runner.py`**:  
  Định nghĩa hàm `run_model(...)` để xây dựng pipeline:  
  - Tiền xử lý dữ liệu (imputation, scaling, encoding).  
  - Giảm chiều dữ liệu bằng PCA.  
  - Huấn luyện mô hình (Logistic Regression, SVM, Random Forest).  
  - Trả về metrics (Accuracy, Precision, Recall, F1, Explained Variance %).  

---
## Assignment 2 (comming soon)

## Assignment 3 (comming soon)

## Phần mở rộng (comming soon)
---

##  Hướng dẫn chạy notebook
- Mở notebook **`Assignment1_CEML2.ipynb`** trong Google Colab.  
- Chọn **Runtime → Run All**.  
- Notebook đã được cấu hình sẵn: import thư viện, tải dataset, xử lý và chạy mô hình.  
- Sau khi chạy, bạn sẽ có ngay kết quả huấn luyện và đánh giá.  

---

## Cấu trúc dự án
```
MachineLearning_Assignment/
├── Assignment1/
│   ├── data/
│   │   └── mobiles_uncleaned.csv
│   ├── modules/
│   │   ├── features_extractor.py
│   │   ├── model_runner.py
│   │   └── __init__.py
│   └── notebooks/
│       └── Assignment1_CEML2.ipynb
│
├── Assignment2/
│   ├── data/
│   ├── modules/
│   └── notebooks/
│
├── Assignment3/
│   ├── data/
│   ├── modules/
│   └── notebooks/
│
└── README.md

```

## Notebook
 
- [Link notebook](https://colab.research.google.com/drive/1saG65yL3ieFIaZLorNRLfMgdfchSFudX?usp=sharing)

---

## Liên hệ
Nếu có thắc mắc, vui lòng liên hệ:  
- **Trương Thiên Ân** – an.truong241105@hcmut.edu.vn  
- **Lại Nguyễn Hoàng Hưng** – hung.lai2805@hcmut.edu.vn  
- **Nguyễn Tô Quốc Việt** – viet.nguyenluminous@hcmut.edu.vn  

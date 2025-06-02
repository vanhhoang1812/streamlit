# 📊 Trực Quan Hóa Dữ Liệu Giao Dịch Người Dùng

## 🧾 Giới Thiệu Dataset

Dataset này chứa thông tin chi tiết về **giao dịch của người dùng**, bao gồm các đặc điểm nhân khẩu học và hành vi mua sắm. Dữ liệu này đặc biệt hữu ích cho các mục tiêu như:

- Phân tích xu hướng tiêu dùng 🛍️  
- Hiểu tác động của nhân khẩu học đến hành vi mua sắm 👥  
- Phân khúc thị trường theo khu vực, độ tuổi, giới tính và sản phẩm 🌍

### 🧩 Các trường dữ liệu bao gồm:

- 🆔 **User ID**: Mã định danh duy nhất cho mỗi người dùng để theo dõi giao dịch.  
- 🎂 **Age**: Tuổi của người dùng tại thời điểm mua hàng — yếu tố ảnh hưởng đến thói quen chi tiêu.  
- 🚻 **Gender**: Giới tính của người dùng — hỗ trợ phân tích theo giới.  
- 🌐 **Country**: Quốc gia nơi người dùng sinh sống — phục vụ phân tích thị trường theo vùng.  
- 💰 **Purchase Amount**: Tổng số tiền chi tiêu trong mỗi giao dịch.  
- 📅 **Purchase Date**: Ngày thực hiện giao dịch — dùng để phân tích theo thời gian.  
- 🛒 **Product Category**: Danh mục sản phẩm đã mua — giúp khám phá sở thích tiêu dùng.

---
## Cài đặt thư viện cần thiết

Trước tiên, hãy đảm bảo bạn đã cài đặt Python (phiên bản >= 3.7).  
Sau đó, sử dụng lệnh sau để cài đặt các thư viện cần thiết từ file `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Chạy ứng dụng với Streamlit
Sau khi cài đặt xong, chạy ứng dụng bằng lệnh sau:

```bash
streamlit run Home.py
```
Ứng dụng sẽ khởi chạy trong trình duyệt tại địa chỉ mặc định: http://localhost:8501

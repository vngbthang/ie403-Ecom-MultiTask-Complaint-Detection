# Hướng dẫn Cài đặt Môi trường (Windows & VS Code)

Để có thể chạy code dự án mà không gặp lỗi xung đột phiên bản thư viện, tất cả thành viên **BẮT BUỘC** phải thiết lập môi trường ảo theo các bước sau.

## Bước 1: Clone Repository
Mở terminal trong VS Code (phím tắt `Ctrl + \``) và chạy lệnh:
```cmd
git clone <URL_CUA_REPO>
cd <TEN_THU_MUC_REPO>
```

## Bước 2: Tạo môi trường ảo
Môi trường ảo (virtual environment) giúp cô lập thư viện của dự án này khỏi hệ thống máy tính. Chạy lệnh:
```cmd
python -m venv env
```

## Bước 3: Kích hoạt môi trường ảo
Kích hoạt môi trường bằng lệnh sau:
```cmd
.\env\Scripts\activate
```
*Dấu hiệu thành công: Bạn sẽ thấy chữ `(env)` màu xanh xuất hiện ở đầu dòng lệnh terminal.*

## Bước 4: Cài đặt các thư viện cần thiết
Đảm bảo bạn đã kích hoạt môi trường ảo (có chữ `(env)`), sau đó chạy lệnh cài đặt:
```cmd
pip install -r requirements.txt
```
Quá trình này có thể mất vài phút. Sau khi chạy xong, môi trường của bạn đã hoàn toàn sẵn sàng!

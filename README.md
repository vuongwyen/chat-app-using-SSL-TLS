server.py:
Khởi tạo máy chủ: Mở một socket và gắn nó vào cổng đã chỉ định trên máy chủ.
Chấp nhận kết nối từ client: Sử dụng phương thức server.accept() để chấp nhận kết nối từ client. Khi một client kết nối thành công, một socket mới được tạo để giao tiếp với client này.
Bắt đầu giao tiếp bảo mật: Sử dụng ssl.wrap_socket() để bao bọc socket của client trong một lớp SSL/TLS, đảm bảo rằng dữ liệu gửi đi và nhận về được mã hóa và giải mã.
Xác thực và gửi thông tin nickname: Sau khi kết nối bảo mật được thiết lập, máy chủ gửi yêu cầu cho client nhập nickname, và sau đó gửi nickname cho máy chủ.
Gửi và nhận tin nhắn: Máy chủ và client sẽ gửi và nhận tin nhắn qua socket đã được bảo mật bằng TLS. Tin nhắn nhận được từ một client sẽ được phát lại cho tất cả các client khác.
client.py:
Nhập nickname: Người dùng được yêu cầu nhập nickname của họ.
Khởi tạo kết nối: Mở một socket và bắt đầu kết nối với máy chủ.
Bắt đầu giao tiếp bảo mật: Sử dụng ssl.wrap_socket() để bao bọc socket của client trong một lớp SSL/TLS, tạo ra một kênh bảo mật cho giao tiếp.
Gửi và nhận thông tin nickname: Client gửi nickname của mình cho máy chủ sau khi kết nối được thiết lập.
Gửi và nhận tin nhắn: Client có thể gửi và nhận tin nhắn từ máy chủ thông qua kênh bảo mật TLS.

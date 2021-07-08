<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/EE3151_SEM202_PROJECT/main/latex/images/final.PNG" width="900"></p>

<h1 align="center">EE3151 SEM202 PROJECT</h1>

## Lời cảm ơn
Trước tiên, em muốn bày tỏ lòng biết ơn chân thành tới giáo viên hướng dẫn của em, thầy **PGS.TS Hà Hoàng Kha** - "giảng viên bộ môn Viễn Thông khoa Điện--Điện Tử" đã trực tiếp giúp đỡ, hướng dẫn và cho lời khuyên trong việc nghiên cứu, thực hiện, chỉnh sửa và hoàn thiện đồ án.  

Em cũng muốn gửi lời cảm ơn chân thành đến trường **Đại học Bách Khoa TP.HCM - Đại học Quốc gia TP.HCM**, khoa **Điện-Điện Tử**, bộ môn **Viễn Thông** đã cung cấp những kiến thức nền tảng, cách thức học tập và nghiên cứu.
Thật khó để tưởng tượng rằng em sẽ tiếp cận và xử lý đề tài đồ án như thế nào nếu không có những vốn liếng quý báu đó.  

Cũng không thể quên cảm ơn một số anh khoá trên cùng các bạn cùng khoá và một vài cá nhân đã giúp đỡ em rất nhiều trong quá trình tìm hiểu đề tài cũng như thực hiện khảo sát lấy số liệu cho đánh giá kết quả của đồ án.  

Em xin chân thành cảm ơn tất cả.  

<h4>Nguyễn Thành Trung</h4>

## Tóm tắt
Tạo màu cho ảnh xám là một chủ đề nóng hổi và thú vị trong ngành thị giác máy tính trong khoảng hai thập kỉ vừa qua.
Rất nhiều những nghiên cứu đã được thực hiện và cho rất nhiều phương pháp với những kết quả ấn tượng.
Tuy việc tạo màu cho mỗi trường hợp là một bài toán có không ít lời giải vì rất nhiều màu có thể có cùng mức xám.
Dẫn đến việc, với một tấm ảnh xám đầu vào, ta có thể có nhiều phương án màu lựa chọn mà vẫn có được tính chân thực.
Nhưng điều đó không đồng nghĩa với việc đây là một bài toán đơn giản mà trái lại là một vấn đề nan giải.  

Trong đồ án này, hai mô hình mạng đối nghịch tạo sinh có điều kiện - cGAN có bộ sinh kiến trúc Unet xây dựng bằng xương sống chuyển giao từ mạng phân loại ResNet18 và bộ phân biệt kiến trúc PatchGAN 70x70, được triển khai và huấn luyện với tập dữ liệu COCO để xử lý vấn đề này.
Chất lượng mô hình đầu tiên thông qua một cuộc khảo sát thực tế 100 người với thang điểm từ 1 (rất giả) đến 5 (rất thật).
Mô hình thứ hai là mô hình được cải thiện bằng cách đưa ra thay đổi nhỏ trong hàm mất và tăng số lượng dữ liệu huấn luyện.
Chất lượng của hai mô hình được so sánh định tính qua những kết quả thử nghiệm, cũng như định lượng qua hai giá trị MSE và RMSE của mỗi mô hình.  

Bên cạnh đó, xây dựng một API tạo màu bằng khung phần mềm Django của Python, từ đó triển khai một ứng dụng web đơn giản để tạo màu cho ảnh bằng khung phần mềm VueJS của Javascript.

<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/EE3151_SEM202_PROJECT/main/latex/images/demoweb.png" width="1000"></p>

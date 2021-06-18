<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/EE3151_SEM202_PROJECT/main/latex/images/final.PNG" width="900"></p>

<h1 align="center">EE3151 SEM202 PROJECT</h1>

## Lời cảm ơn
Trước tiên, em muốn bày tỏ lòng biết ơn chân thành tới giáo viên hướng dẫn của em, thầy **PGS.TS Hà Hoàng Kha** - giảng viên bộ môn Viễn Thông khoa Điện-Điện Tử đã trực tiếp giúp đỡ, hướng dẫn và cho lời khuyên.  
Em cũng muốn gửi lời cảm ơn chân thành đến trường Đại học Bách Khoa TP.HCM, khoa Điện-Điện Tử, bộ môn Viễn Thông đã tạo mọi điều kiện để em có thể hoàn thành tốt đồ án của mình.  
Cảm ơn các anh chị khoá trên cùng các bạn cùng khoa và một số cá nhân đã giúp đỡ em rất nhiều trong quá trình tìm hiểu đề tài cũng như thực hiện khảo sát lấy số liệu cho nghiên cứu của đồ án.

## Tóm tắt
Tạo màu cho ảnh xám là một chủ đề nóng hổi và thú vị trong ngành thị giác máy tính trong khoảng hai thập kỉ vừa qua. Rất nhiều những nghiên cứu đã được thực hiện và cho rất nhiều phương pháp với những kết quả ấn tượng. Tuy việc tạo màu cho mỗi trường hợp là một bài toán có không ít lời giải vì rất nhiều màu có thể có cùng mức xám. Với một tấm ảnh xám đầu vào, ta có thể có nhiều phương án màu lựa chọn mà vẫn có được tính chân thực. Nhưng điều đó không đồng nghĩa với việc đây là một bài toán đơn giản mà trái lại là một vấn đề nan giải.  
Trong đồ án này, một mô hình mạng đối nghịch tạo sinh có điều kiện - cGAN có bộ sinh kiến trúc Unet xây dựng bằng xương sống chuyển giao từ mạng phân loại ResNet18 và bộ phân biệt kiến trúc PatchGAN 70x70, được triển khai và huấn luyện với tập dữ liệu 10,000 bức ảnh của tập dữ liệu COCO để xử lí vấn đề này. Chất lượng mô hình thông qua một cuộc khảo sát thực tế 100 người được đánh giá ở mức trung bình-khá.  
Bên cạnh đó, xây dựng được một API tạo màu bằng khung phần mềm Django của Python, từ đó triển khai một ứng dụng web đơn giản để tạo màu cho ảnh bằng khung phần mềm VueJS của Javascript.

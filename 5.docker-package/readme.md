* Tại sao chúng ta cần phải đóng gói model lại?
    - Đôi lúc, chúng ta cần phải chia sẻ model / ứng dụng với những người khác. Và khi họ chạy các ứng dụng thì đa số gặp vấn đề vì hệ điều hành khác nhau, thư viện khác. Vì vậy, để những người khác có thể sử dụng được model, chúng ta cần phải đóng gói model lại cũng như là các thành phần của model.
    - Giải pháp để giải quyết vấn đề trên là sử dụng <code>container</code>.
    - Bằng cách container/package, chung ta có thể chia sẻ model với những người khác, có thể chạy trên các server khác nhau, google, aws

🛳 Basics of Docker
<code>Docker</code> là một công cụ quản lí <code>container</code>, gói ứng dụng, các thành phần phụ thuộc vào <code>image</code> di dộng có thể được chia sẻ và chạy trên bất kì nền tảng hệ thống nào.

<b>Docker có 3 thành phần chính:</b>
    <li>Docker File</li>
    <li>Docker Image</li>
    <li>Docker Container</li>

* Tệp <code>Docker File</code> chứa danh sách các lệnh cần chạy như các lệnh: dependeces, run, command,...
* <code>Docker Image</code> là một gói phần mềm nhẹ, độc lập, có thể thực thi(được xây dựng từ docker file) bao gồm mọi thứ cần thiết để chạy ứng dụng: code, runtime, system tools, system libraries, ...
* <code>Docker Container</code> là một phiên bản của Docker Image chứ ứng dụng đang chạy
<img src="https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fdocker%2Fdocker_arch.png&w=3840&q=75">


🚢 Docker Compose
* Docker Compose là một công cụ để xác định và chạy multi-container trong ứng dụng Docker. Với Compose, chúng ta có thể tạo ra một tệp yaml để chỉ ra các thành phần cần chạy.
* 
<pre class="language-yaml"><code class="language-yaml"><span class="">version</span><span class="text-code-white">:</span> <span class="text-code-green">'3'</span>
<span class="">services</span><span class="text-code-white">:</span>
  <span class="">prediction_api</span><span class="text-code-white">:</span>
    <span class="">build</span><span class="text-code-white">:</span> .
    <span class="">container_name</span><span class="text-code-white">:</span> <span class="text-code-green">'inference_container'</span>
    <span class="">ports</span><span class="text-code-white">:</span>
      <span class="text-code-white">-</span> <span class="text-code-green">'8000:8000'</span>
</code></pre>

* Run FastAPI:
  - uvicorn app:app --port 8000 --reload
  - http://localhost:8000/docs sẽ trông như thế này:
  <img src="https://www.ravirajag.dev/_next/image?url=%2Fstatic%2Fimages%2Fdocker%2Ffastapi_2.png&w=3840&q=75">
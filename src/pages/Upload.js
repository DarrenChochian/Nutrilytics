// src/pages/Upload.js
import { useState } from "react";

export default function Upload() {
  const [image, setImage] = useState(null);

  const handleUpload = (e) => {
    const file = e.target.files[0];
    setImage(file);
  };

  const handleSubmit = async () => {
    const formData = new FormData();
    formData.append("file", image);
    await fetch("http://localhost:8000/upload", {
      method: "POST",
      body: formData,
    });
  };

  return (
    <div>
      <input type="file" onChange={handleUpload} />
      <button onClick={handleSubmit}>Upload</button>
    </div>
  );
}

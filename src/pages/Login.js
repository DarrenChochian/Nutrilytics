// src/pages/Login.js
import React, { useRef, useState } from "react";
import { signInWithEmailAndPassword } from "firebase/auth";
import { auth } from "../firebase";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const emailRef    = useRef();
  const passwordRef = useRef();
  const navigate    = useNavigate();
  const [error, setError] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");
    try {
      await signInWithEmailAndPassword(
        auth,
        emailRef.current.value,
        passwordRef.current.value
      );
      navigate("/dashboard");
    } catch (err) {
      setError("Invalid credentials");
    }
  }

  return (
    <div className="flex flex-col items-center mt-10">
      <h2 className="text-2xl font-bold mb-4">Log In</h2>
      {error && <p className="text-red-500 mb-2">{error}</p>}
      <form onSubmit={handleSubmit} className="flex flex-col gap-3 w-80">
        <input
          type="email"
          ref={emailRef}
          placeholder="Email"
          className="border p-2 rounded"
          required
        />
        <input
          type="password"
          ref={passwordRef}
          placeholder="Password"
          className="border p-2 rounded"
          required
        />
        <button className="bg-green-600 text-white py-2 rounded hover:bg-green-700">
          Log In
        </button>
      </form>
    </div>
  );
}

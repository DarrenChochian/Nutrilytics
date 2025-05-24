// src/pages/Signup.js
import React, { useRef, useState } from "react";
import { createUserWithEmailAndPassword } from "firebase/auth";
import { auth } from "../firebase";
import { useNavigate } from "react-router-dom";

export default function Signup() {
  const emailRef    = useRef();
  const passwordRef = useRef();
  const navigate    = useNavigate();
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");
    try {
      setLoading(true);
      await createUserWithEmailAndPassword(
        auth,
        emailRef.current.value,
        passwordRef.current.value
      );
      navigate("/dashboard");                    // go to a protected page
    } catch (err) {
      setError(err.message.replace("Firebase:", ""));
    }
    setLoading(false);
  }

  return (
    <div className="flex flex-col items-center mt-10">
      <h2 className="text-2xl font-bold mb-4">Sign Up</h2>
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
        <button
          disabled={loading}
          className="bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
        >
          Sign Up
        </button>
      </form>
    </div>
  );
}

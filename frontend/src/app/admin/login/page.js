"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { apiRequest } from "@/lib/api";

export default function AdminLoginPage() {

  const router = useRouter();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleLogin(e) {

    e.preventDefault();

    setLoading(true);
    setError("");

    try {

      const data = await apiRequest(
        "/api/auth/login",
        {
          method: "POST",
          body: JSON.stringify({
            email,
            password
          })
        }
      );

      localStorage.setItem(
        "admin_token",
        data.access_token
      );

      router.push("/admin");

    } catch (error) {

      setError(
        "Invalid email or password"
      );

    } finally {

      setLoading(false);

    }

  }

  return (
    <main className="min-h-screen bg-gray-950 text-white flex items-center justify-center">

      <form
        onSubmit={handleLogin}
        className="bg-gray-900 border border-gray-800 rounded-2xl p-8 w-full max-w-md"
      >

        <h1 className="text-3xl font-bold text-cyan-400 mb-6">
          Recruiter Login
        </h1>

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) =>
            setEmail(e.target.value)
          }
          className="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 mb-4"
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) =>
            setPassword(e.target.value)
          }
          className="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3 mb-4"
        />

        {error && (
          <p className="text-red-400 mb-4">
            {error}
          </p>
        )}

        <button
          type="submit"
          disabled={loading}
          className="w-full bg-cyan-600 hover:bg-cyan-700 py-3 rounded-lg font-semibold"
        >
          {loading
            ? "Logging In..."
            : "Login"}
        </button>

      </form>

    </main>
  );
}
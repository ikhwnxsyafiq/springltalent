"use client";

import { useEffect, useState } from "react";
import { apiRequest } from "@/lib/api";

export default function TestApiPage() {
  const [message, setMessage] = useState("Testing backend connection...");

  useEffect(() => {
    async function testBackend() {
      try {
        const data = await apiRequest("/");
        setMessage(data.message || "Backend connected successfully");
      } catch (error) {
        setMessage(error.message);
      }
    }

    testBackend();
  }, []);

  return (
    <main className="min-h-screen flex items-center justify-center bg-gray-950 text-white">
      <div className="rounded-xl border border-gray-800 bg-gray-900 p-8">
        <h1 className="text-2xl font-bold">Backend Connection Test</h1>
        <p className="mt-4 text-gray-300">{message}</p>
      </div>
    </main>
  );
}
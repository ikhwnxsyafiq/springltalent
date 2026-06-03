"use client";
import { useState } from "react";

export default function RegisterPage() {
  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    password: "",
    confirmPassword: "",
    university: "",
  });
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    setError("");

    if (formData.password !== formData.confirmPassword) {
      setError("Passwords do not match!");
      return;
    }

    setLoading(true);
    // API call will go here later
    console.log("Register:", formData);
    setTimeout(() => setLoading(false), 1500);
  };

  return (
    <div className="min-h-screen bg-gray-950 flex items-center justify-center px-4 py-10">
      <div className="w-full max-w-md">

        {/* Logo */}
        <div className="text-center mb-8">
          <h1 className="text-3xl font-bold text-white">🧑‍💻 SpringTalent</h1>
          <p className="text-gray-400 mt-2">IC Design Assessment Platform</p>
        </div>

        {/* Card */}
        <div className="bg-gray-900 rounded-2xl p-8 shadow-xl border border-gray-800">
          <h2 className="text-xl font-semibold text-white mb-6">
            Create your account
          </h2>

          {/* Error message */}
          {error && (
            <div className="bg-red-900 border border-red-700 text-red-300 
                            rounded-lg px-4 py-3 mb-4 text-sm">
              ❌ {error}
            </div>
          )}

          <form onSubmit={handleRegister} className="space-y-4">

            {/* Full Name */}
            <div>
              <label className="block text-sm text-gray-400 mb-1">
                Full Name
              </label>
              <input
                type="text"
                name="fullName"
                value={formData.fullName}
                onChange={handleChange}
                placeholder="Muhammad Ikhwan"
                required
                className="w-full bg-gray-800 text-white rounded-lg px-4 py-3 
                           border border-gray-700 focus:outline-none 
                           focus:border-blue-500 placeholder-gray-500"
              />
            </div>

            {/* University */}
            <div>
              <label className="block text-sm text-gray-400 mb-1">
                University
              </label>
              <input
                type="text"
                name="university"
                value={formData.university}
                onChange={handleChange}
                placeholder="e.g. Universiti Malaya"
                required
                className="w-full bg-gray-800 text-white rounded-lg px-4 py-3 
                           border border-gray-700 focus:outline-none 
                           focus:border-blue-500 placeholder-gray-500"
              />
            </div>

            {/* Email */}
            <div>
              <label className="block text-sm text-gray-400 mb-1">
                Email address
              </label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                placeholder="you@example.com"
                required
                className="w-full bg-gray-800 text-white rounded-lg px-4 py-3 
                           border border-gray-700 focus:outline-none 
                           focus:border-blue-500 placeholder-gray-500"
              />
            </div>

            {/* Password */}
            <div>
              <label className="block text-sm text-gray-400 mb-1">
                Password
              </label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                placeholder="••••••••"
                required
                className="w-full bg-gray-800 text-white rounded-lg px-4 py-3 
                           border border-gray-700 focus:outline-none 
                           focus:border-blue-500 placeholder-gray-500"
              />
            </div>

            {/* Confirm Password */}
            <div>
              <label className="block text-sm text-gray-400 mb-1">
                Confirm Password
              </label>
              <input
                type="password"
                name="confirmPassword"
                value={formData.confirmPassword}
                onChange={handleChange}
                placeholder="••••••••"
                required
                className="w-full bg-gray-800 text-white rounded-lg px-4 py-3 
                           border border-gray-700 focus:outline-none 
                           focus:border-blue-500 placeholder-gray-500"
              />
            </div>

            {/* Button */}
            <button
              type="submit"
              disabled={loading}
              className="w-full bg-blue-600 hover:bg-blue-700 text-white 
                         font-semibold py-3 rounded-lg transition-colors
                         disabled:opacity-50 disabled:cursor-not-allowed mt-2"
            >
              {loading ? "Creating account..." : "Create Account"}
            </button>

          </form>

          {/* Login link */}
          <p className="text-center text-gray-400 text-sm mt-6">
            Already have an account?{" "}
            <a href="/login" className="text-blue-400 hover:underline">
              Sign in here
            </a>
          </p>

        </div>
      </div>
    </div>
  );
}
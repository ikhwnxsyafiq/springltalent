"use client";
import Link from "next/link";

export default function DashboardPage() {
  // Dummy user data (will be replaced with real API later)
  const user = {
    name: "Muhammad Ikhwan",
    university: "Universiti Malaya",
    email: "ikhwan@example.com",
    hasAttempted: false,
  };

  return (
    <div className="min-h-screen bg-gray-950 text-white">

      {/* Navbar */}
      <nav className="flex items-center justify-between px-8 py-5 border-b border-gray-800">
        <h1 className="text-xl font-bold">🧑‍💻 SpringTalent</h1>
        <div className="flex items-center gap-4">
          <span className="text-gray-400 text-sm">Hi, {user.name}</span>
          <Link href="/login"
            className="text-sm text-gray-400 hover:text-white transition-colors">
            Logout
          </Link>
        </div>
      </nav>

      {/* Main Content */}
      <div className="max-w-4xl mx-auto px-6 py-12">

        {/* Welcome */}
        <div className="mb-10">
          <h2 className="text-3xl font-bold">Welcome, {user.name}! 👋</h2>
          <p className="text-gray-400 mt-2">{user.university}</p>
        </div>

        {/* Status Card */}
        <div className="bg-gray-900 border border-gray-800 rounded-2xl p-8 mb-8">
          {user.hasAttempted ? (
            <div>
              <p className="text-green-400 font-semibold text-lg">
                ✅ Assessment Completed
              </p>
              <p className="text-gray-400 mt-2">
                You have already completed your assessment.
              </p>
              <Link href="/results"
                className="inline-block mt-4 bg-blue-600 hover:bg-blue-700 
                           text-white font-semibold px-6 py-3 rounded-lg 
                           transition-colors">
                View My Results
              </Link>
            </div>
          ) : (
            <div>
              <p className="text-yellow-400 font-semibold text-lg">
                ⏳ Assessment Not Started
              </p>
              <p className="text-gray-400 mt-2 mb-6">
                You have not taken your IC Design assessment yet. 
                The test consists of 20 questions across 4 domains 
                and takes approximately 30-45 minutes.
              </p>

              {/* Assessment Info */}
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                {[
                  { label: "Questions", value: "20" },
                  { label: "Duration", value: "45 mins" },
                  { label: "Domains", value: "4" },
                  { label: "Attempts", value: "1 only" },
                ].map((item) => (
                  <div key={item.label}
                    className="bg-gray-800 rounded-xl p-4 text-center">
                    <p className="text-2xl font-bold text-blue-400">
                      {item.value}
                    </p>
                    <p className="text-gray-400 text-sm mt-1">{item.label}</p>
                  </div>
                ))}
              </div>

              <Link href="/assessment"
                className="inline-block bg-blue-600 hover:bg-blue-700 
                           text-white font-semibold px-8 py-3 rounded-lg 
                           transition-colors">
                Start Assessment →
              </Link>
            </div>
          )}
        </div>

        {/* Domains */}
        <h3 className="text-xl font-semibold mb-4">What will be assessed</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {[
            { icon: "⚡", title: "Digital Design", desc: "RTL, timing analysis, logic synthesis", questions: "5 questions" },
            { icon: "📡", title: "Analog Design", desc: "Circuit theory, amplifiers, filters", questions: "5 questions" },
            { icon: "🔲", title: "Physical Backend", desc: "Floorplanning, routing, signoff", questions: "5 questions" },
            { icon: "🔀", title: "Mixed-Signal", desc: "ADC, DAC, interface design", questions: "5 questions" },
          ].map((domain) => (
            <div key={domain.title}
              className="bg-gray-900 border border-gray-800 rounded-xl p-5
                         hover:border-blue-800 transition-colors">
              <div className="flex items-start justify-between">
                <div>
                  <span className="text-2xl">{domain.icon}</span>
                  <h4 className="font-semibold mt-2">{domain.title}</h4>
                  <p className="text-gray-400 text-sm mt-1">{domain.desc}</p>
                </div>
                <span className="text-blue-400 text-xs bg-blue-900 
                                 px-2 py-1 rounded-full">
                  {domain.questions}
                </span>
              </div>
            </div>
          ))}
        </div>

      </div>
    </div>
  );
}
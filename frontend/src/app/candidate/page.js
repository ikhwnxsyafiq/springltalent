"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { apiRequest } from "@/lib/api";

export default function CandidatePage() {

  const router = useRouter();

  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [university, setUniversity] = useState("");
  const [programme, setProgramme] = useState("");
  const [cgpa, setCgpa] = useState("");
  const [graduationYear, setGraduationYear] = useState("");

  const [loading, setLoading] = useState(false);

  const handleStartAssessment = async () => {

    if (
      !fullName ||
      !email ||
      !university ||
      !programme ||
      !cgpa ||
      !graduationYear
    ) {
      alert("Please complete all fields.");
      return;
    }

    try {

      setLoading(true);

      const data = await apiRequest(
        "/api/candidate/",
        {
          method: "POST",
          body: JSON.stringify({
            full_name: fullName,
            email,
            university,
            programme,
            cgpa,
            graduation_year: graduationYear
          })
        }
      );

      localStorage.setItem(
        "candidate_id",
        data.candidate_id
      );

      router.push("/assessment");

    } catch (error) {

      alert(error.message);

    } finally {

      setLoading(false);

    }

  };

  return (
    <main className="min-h-screen bg-gray-950 text-white flex items-center justify-center px-4">

      <div className="w-full max-w-3xl bg-gray-900 border border-gray-800 rounded-2xl p-8">

        <h1 className="text-3xl font-bold">
          Candidate Information
        </h1>

        <p className="text-gray-400 mt-2">
          Complete your information before starting the assessment.
        </p>

        <div className="mt-8 space-y-5">

          <input
            type="text"
            placeholder="Full Name"
            value={fullName}
            onChange={(e) =>
              setFullName(e.target.value)
            }
            className="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3"
          />

          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) =>
              setEmail(e.target.value)
            }
            className="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3"
          />

          <input
            type="text"
            placeholder="University"
            value={university}
            onChange={(e) =>
              setUniversity(e.target.value)
            }
            className="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3"
          />

          <input
            type="text"
            placeholder="Programme"
            value={programme}
            onChange={(e) =>
              setProgramme(e.target.value)
            }
            className="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3"
          />

          <input
            type="text"
            placeholder="CGPA"
            value={cgpa}
            onChange={(e) =>
              setCgpa(e.target.value)
            }
            className="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3"
          />

          <input
            type="text"
            placeholder="Graduation Year"
            value={graduationYear}
            onChange={(e) =>
              setGraduationYear(e.target.value)
            }
            className="w-full bg-gray-800 border border-gray-700 rounded-lg px-4 py-3"
          />

          <button
            onClick={handleStartAssessment}
            disabled={loading}
            className="w-full bg-cyan-600 hover:bg-cyan-700 py-3 rounded-lg font-semibold"
          >
            {loading
              ? "Creating Candidate..."
              : "Start Assessment"}
          </button>

        </div>

      </div>

    </main>
  );
}
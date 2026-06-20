"use client";

import { useEffect, useState } from "react";
import { useParams, useRouter } from "next/navigation";
import { apiRequest } from "@/lib/api";

export default function CandidateDetailPage() {

  const params = useParams();
  const router = useRouter();

  const [candidate, setCandidate] = useState(null);
  const [report, setReport] = useState(null);
  const [resume, setResume] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {

    const token = localStorage.getItem(
      "admin_token"
    );

    if (!token) {
      router.push("/admin/login");
      return;
    }

    async function loadCandidate() {

      try {

        const candidateData = await apiRequest(
          `/api/candidate/${params.id}`
        );

        setCandidate(candidateData);

        try {

          const reportData = await apiRequest(
            `/api/candidate/${params.id}/report`
          );

          setReport(reportData);

        } catch {

          setReport(null);

        }

        try {

          const resumeData = await apiRequest(
            `/api/resume/candidate/${params.id}`
          );

          setResume(resumeData);

        } catch {

          setResume(null);

        }

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);

      }

    }

    loadCandidate();

  }, [params.id, router]);

  if (loading) {
    return (
      <main className="min-h-screen bg-gray-950 text-white flex items-center justify-center">
        Loading Candidate...
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gray-950 text-white p-8">

      <h1 className="text-4xl font-bold text-cyan-400 mb-8">
        Candidate Profile
      </h1>

      <div className="bg-gray-900 border border-gray-800 rounded-2xl p-8">

        <div className="grid md:grid-cols-2 gap-6">

          <div>
            <p className="text-gray-400">Full Name</p>
            <p>{candidate?.full_name}</p>
          </div>

          <div>
            <p className="text-gray-400">Email</p>
            <p>{candidate?.email}</p>
          </div>

          <div>
            <p className="text-gray-400">University</p>
            <p>{candidate?.university}</p>
          </div>

          <div>
            <p className="text-gray-400">Programme</p>
            <p>{candidate?.programme}</p>
          </div>

          <div>
            <p className="text-gray-400">CGPA</p>
            <p>{candidate?.cgpa}</p>
          </div>

          <div>
            <p className="text-gray-400">Graduation Year</p>
            <p>{candidate?.graduation_year}</p>
          </div>

        </div>

      </div>

      {resume && (

        <div className="bg-gray-900 border border-gray-800 rounded-2xl p-8 mt-8">

          <h2 className="text-2xl font-bold text-cyan-400 mb-6">
            Resume Information
          </h2>

          <div className="grid md:grid-cols-2 gap-6">

            <div>
              <p className="text-gray-400">
                Resume File
              </p>

              <p>
                {resume.file_name}
              </p>

              <a
                href={`http://127.0.0.1:8000/api/resume/download/${params.id}`}
                target="_blank"
                rel="noopener noreferrer"
                className="inline-block mt-4 bg-cyan-600 hover:bg-cyan-700 px-4 py-2 rounded-lg"
              >
                Download Resume
              </a>
            </div>

            <div>
              <p className="text-gray-400">
                Candidate ID
              </p>

              <p>
                {resume.candidate_id}
              </p>
            </div>

          </div>

        </div>

      )}

      {report && (

        <div className="bg-gray-900 border border-gray-800 rounded-2xl p-8 mt-8">

          <div className="flex justify-between items-center mb-6">
            <h2 className="text-2xl font-bold text-cyan-400">
              Assessment Results
            </h2>
            <button
              disabled
              className="bg-gray-700 text-gray-400 px-4 py-2 rounded-lg cursor-not-allowed"
            >
              PDF Report (Coming Soon)
            </button>
          </div>

          <div className="grid md:grid-cols-3 gap-6">

            <div>
              <p className="text-gray-400">
                Overall Score
              </p>

              <p className="text-3xl font-bold text-green-400">
                {report.overall_score}%
              </p>
            </div>

            <div>
              <p className="text-gray-400">
                Recommended Role
              </p>

              <p>
                {report.recommendation?.recommended_role}
              </p>
            </div>

            <div>
              <p className="text-gray-400">
                Career Fit Score
              </p>

              <p>
                {report.recommendation?.career_fit_score}%
              </p>
            </div>

          </div>

        </div>

      )}

    </main>
  );
}
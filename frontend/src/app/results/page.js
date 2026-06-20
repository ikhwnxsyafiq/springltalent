"use client";

import { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import { apiRequest } from "@/lib/api";

import {
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  Radar,
  ResponsiveContainer,
} from "recharts";


const DOMAIN_LABELS = {
  digital_design: "Digital Design",
  analog_design: "Analog Design",
  backend: "Physical Design",
  mixed_signal: "Mixed Signal",
  verification: "Verification",
  eda_tools: "EDA Tools",
};


export default function ResultsPage() {
  
  
  const searchParams = useSearchParams();

  const sessionId = searchParams.get("session_id");

  const [report, setReport] = useState(null);
  const [candidate, setCandidate] = useState(null);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadResults() {
      try {
        if (!sessionId) {
          setError("Session ID not found.");
          return;
        }

        const data = await apiRequest(
          `/api/assessment/result/${sessionId}`
        );

        setReport(data);

        const candidateId =
          localStorage.getItem("candidate_id");

        if (candidateId) {

          const candidateData = 
            await apiRequest(
              `/api/candidate/${candidateId}`
            );

          setCandidate(candidateData);
        }

      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    loadResults();
  }, [sessionId]);

  if (loading) {
    return (
      <main className="min-h-screen bg-gray-950 text-white flex items-center justify-center">
        Loading assessment results...
      </main>
    );
  }

  if (error) {
    return (
      <main className="min-h-screen bg-gray-950 text-red-400 flex items-center justify-center">
        {error}
      </main>
    );
  }

  const assessmentType = localStorage.getItem("assessment_type");

  const recommendation = report?.recommendation || {};
  const aiFeedback = report?.ai_feedback || {};
  const skillGaps = report?.skill_gaps || [];


  if (assessmentType === "quick") {
    return (
      <main className="min-h-screen bg-gray-950 text-white flex items-center justify-center">
        <div className="bg-gray-900 border border-gray-800 rounded-2xl p-10 text-center">
          <h1 className="text-2xl font-bold text-cyan-400 mb-6">
            Quick Assessment Results
          </h1>

          <p className="text-6xl font-bold text-green-400">
            {report?.overall_score || 0}%
          </p>

          <p className="mt-6 text-gray-400">
            This is a practice assessment only.
          </p>

          <p className="mt-2 text-gray-400">
            Complete the Full Assessment to unlock detailed insights and recommendations
          </p>

          <ul className="mt-4 text-left text-gray-300 space-y-2">
            <li>✅ Skill Competency Radar</li>
            <li>✅ AI Career Feedback</li>
            <li>✅ Career Recommendation</li>
            <li>✅ Skill Gap Analysis</li>
            <li>✅ Hiring Targets</li>
            <li>✅ PDF Assessment Report</li>
          </ul>
        </div>
      </main>
    );
  }


  const radarData =
  report?.skill_mapping?.radar_chart || [];

  return (
    <main className="min-h-screen bg-gray-950 text-white px-6 py-10">
      <div className="max-w-6xl mx-auto">

        <div className="mb-8">
          <h1 className="text-4xl font-bold text-cyan-400">
            SpringTalent Assessment Results
          </h1>

          <p className="text-gray-400 mt-2">
            IC Design Recruitment System & Assessment Engine
          </p>
        </div>

        {candidate && (
          <div className="mb-8 bg-gray-900 border border-gray-800 rounded-2xl p-6">

            <h2 className="text-xl font-semibold mb-4 text-cyan-400">
              Candidate Information Test
            </h2>

            <div className="grid md:grid-cols-2 gap-4">

              <div>
                <p className="text-gray-400">Full Name</p>
                <p>{candidate.full_name}</p>
              </div>

              <div>
                <p className="text-gray-400">Email</p>
                <p>{candidate.email}</p>
              </div>

              <div>
                <p className="text-gray-400">University</p>
                <p>{candidate.university}</p>
              </div>

              <div>
                <p className="text-gray-400">Programme</p>
                <p>{candidate.programme}</p>
              </div>

              <div>
                <p className="text-gray-400">CGPA</p>
                <p>{candidate.cgpa}</p>
              </div>

              <div>
                <p className="text-gray-400">Graduation Year</p>
                <p>{candidate.graduation_year}</p>
              </div>

            </div>

          </div>
        )}

        {/* Summary Cards */}

        <div className="grid md:grid-cols-3 gap-6">

          <div className="bg-gray-900 border border-gray-800 rounded-2xl p-6">
            <h2 className="text-gray-400 text-sm uppercase mb-2">
              Overall Score
            </h2>

            <p className="text-5xl font-bold text-cyan-400">
              {report.overall_score}%
            </p>
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-2xl p-6">
            <h2 className="text-gray-400 text-sm uppercase mb-2">
              Recommended Role
            </h2>

            <p className="text-xl font-semibold">
              {recommendation.recommended_role}
            </p>
          </div>

          <div className="bg-gray-900 border border-gray-800 rounded-2xl p-6">
            <h2 className="text-gray-400 text-sm uppercase mb-2">
              Career Fit Score
            </h2>

            <p className="text-5xl font-bold text-green-400">
              {recommendation.career_fit_score}%
            </p>
          </div>

        </div>

        {/* Domain Scores */}

        <div className="mt-8 bg-gray-900 border border-gray-800 rounded-2xl p-6">

          <h2 className="text-xl font-semibold mb-4 text-cyan-400">
            Domain Scores
          </h2>

          <div className="grid md:grid-cols-2 gap-4">

            {Object.entries(report.domain_scores || {}).map(
              ([domain, score]) => (
                <div
                  key={domain}
                  className="bg-gray-800 rounded-lg p-4"
                >
                  <p className="font-semibold">
                    {DOMAIN_LABELS[domain] || domain}
                  </p>

                  <p className="text-cyan-400">
                    {score}%
                  </p>
                </div>
              )
            )}

          </div>

        </div>
        
        {/* Skill Competency Radar */}

        <div className="mt-8 bg-gray-900 border border-gray-800 rounded-2xl p-6">

          <h2 className="text-xl font-semibold mb-4 text-cyan-400">
            Skill Competency Radar
          </h2>

          <div className="w-full h-[400px]">

            <ResponsiveContainer width="100%" height="100%">

              <RadarChart data={radarData}>

                <PolarGrid />

                <PolarAngleAxis dataKey="skill" />

                <PolarRadiusAxis
                  angle={90}
                  domain={[0, 100]}
                />

                <Radar
                  dataKey="score"
                  stroke="#22d3ee"
                  fill="#22d3ee"
                  fillOpacity={0.4}
                />

              </RadarChart>

            </ResponsiveContainer>

          </div>

        </div>

        {/* AI Feedback */}

        <div className="mt-8 bg-gray-900 border border-gray-800 rounded-2xl p-6">

          <h2 className="text-xl font-semibold mb-4 text-cyan-400">
            AI Career Feedback
          </h2>

          <p className="mb-4">
            <strong>Core Strengths:</strong>
            <br />
            {aiFeedback.core_strengths}
          </p>

          <p>
            <strong>Growth Areas:</strong>
            <br />
            {aiFeedback.growth_areas}
          </p>

        </div>

        {/* Learning Roadmap */}

        <div className="mt-8 bg-gray-900 border border-gray-800 rounded-2xl p-6">

          <h2 className="text-xl font-semibold mb-4 text-cyan-400">
            Learning Roadmap
          </h2>

          <ul className="list-disc ml-6 space-y-2">

            {(aiFeedback.roadmap || []).map(
              (item, index) => (
                <li key={index}>
                  {item}
                </li>
              )
            )}

          </ul>

        </div>

        {/* Hiring Targets */}

        <div className="mt-8 bg-gray-900 border border-gray-800 rounded-2xl p-6">

          <h2 className="text-xl font-semibold mb-4 text-cyan-400">
            Hiring Targets
          </h2>

          <ul className="list-disc ml-6 space-y-2">

            {(aiFeedback.hiring_targets || []).map(
              (company, index) => (
                <li key={index}>
                  {company}
                </li>
              )
            )}

          </ul>

        </div>

        {/* Skill Gaps */}

        <div className="mt-8 bg-gray-900 border border-gray-800 rounded-2xl p-6">

          <h2 className="text-xl font-semibold mb-4 text-cyan-400">
            Skill Gap Analysis
          </h2>

          <div className="space-y-3">

            {skillGaps.map((gap, index) => (
              <div
                key={index}
                className="bg-gray-800 rounded-lg p-4"
              >
                <p>
                  <strong>{gap.skill}</strong>
                </p>

                <p>
                  Current Score: {gap.current_score}
                </p>

                <p>
                  Target Score: {gap.target_score}
                </p>

                <p className="text-red-400">
                  Gap: {gap.gap}
                </p>
              </div>
            ))}

          </div>

        </div>

        {/* PDF Download */}

        <div className="mt-8">

          <a
            href={`http://127.0.0.1:8000/api/assessment/report/${sessionId}`}
            target="_blank"
            rel="noreferrer"
            className="inline-block bg-cyan-600 hover:bg-cyan-700 px-6 py-3 rounded-lg font-semibold"
          >
            Download PDF Report
          </a>

        </div>

      </div>
    </main>
  );
}
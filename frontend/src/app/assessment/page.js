"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { apiRequest } from "@/lib/api";

export default function AssessmentPage() {
  const router = useRouter();

  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState("");
  const [answers, setAnswers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const [selectedBox, setSelectedBox] = useState(""); // track clicked box

  const currentQuestion = questions[currentIndex];

  // Dummy candidate scores for left panel
  const candidates = [
    { name: "Amirah", domain: "Digital Design", score: 98 },
    { name: "Aina", domain: "Analog Design", score: 70 },
    { name: "Ikhwan", domain: "Mixed-Signal", score: 85 },
    { name: "Daniel", domain: "EDA Tools", score: 75 },
  ];

  // Boxes for domains + quick/full assessment
  const boxes = [
    "Digital Design",
    "Analog Design",
    "Physical Backend",
    "Mixed-Signal",
    "Verification",
    "EDA Tools",
    "Quick Assessment",
    "Full Assessment",
  ];

  useEffect(() => {
    async function loadQuestions() {
      try {
        const data = await apiRequest("/api/assessment/generate");
        setQuestions(data.questions || []);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    }
    loadQuestions();
  }, []);

  const handleNext = () => {
    if (!selectedAnswer) {
      setError("Please select an answer before continuing.");
      return;
    }

    setError("");
    const updatedAnswers = [
      ...answers,
      {
        questionId: currentQuestion.id,
        selectedAnswer,
        domain: currentQuestion.domain,
      },
    ];
    setAnswers(updatedAnswers);
    setSelectedAnswer("");

    if (currentIndex + 1 < questions.length) {
      setCurrentIndex(currentIndex + 1);
    } else {
      localStorage.setItem(
        "springtalent_answers",
        JSON.stringify(updatedAnswers)
      );
      router.push("/results");
    }
  };

  if (loading) {
    return (
      <main className="min-h-screen bg-gray-950 text-white flex items-center justify-center">
        Loading assessment...
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gray-950 text-white px-6 py-10">
      <div className="flex gap-6 max-w-6xl mx-auto">

        {/* Left Panel */}
        <div className="w-64 bg-gray-900 border border-gray-800 rounded-2xl p-5 flex flex-col gap-4">
          <h3 className="text-lg font-bold text-blue-400 mb-3">
            Candidate Scores
          </h3>
          {candidates.map((c) => (
            <div
              key={c.name}
              className="bg-gray-800 p-3 rounded-lg border border-gray-700"
            >
              <p className="font-semibold">{c.name}</p>
              <p className="text-sm text-gray-400">
                {c.domain}: {c.score}%
              </p>
            </div>
          ))}
        </div>

        {/* Right Panel */}
        <div className="flex-1">
          {/* Boxes */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
            {boxes.map((box) => (
              <button
                key={box}
                onClick={() => setSelectedBox(box)}
                className={`py-4 px-2 rounded-lg font-semibold text-center transition-colors
                  ${
                    selectedBox === box
                      ? "bg-blue-600 text-white"
                      : "bg-gray-800 text-gray-300 hover:bg-gray-700"
                  }`}
              >
                {box}
              </button>
            ))}
          </div>

          {/* Question/Test Panel */}
          {selectedBox && (
            <div className="bg-gray-900 border border-gray-800 rounded-2xl p-8">
              <h2 className="text-xl font-semibold mb-4">
                {selectedBox} Question/Test
              </h2>

              {currentQuestion ? (
                <>
                  <p className="mb-4">{currentQuestion.question_text}</p>
                  {["A", "B", "C", "D"].map((key) => (
                    <button
                      key={key}
                      type="button"
                      onClick={() => setSelectedAnswer(key)}
                      className={`w-full text-left rounded-xl border px-5 py-4 mb-2 transition-colors ${
                        selectedAnswer === key
                          ? "border-blue-500 bg-blue-900/40"
                          : "border-gray-700 bg-gray-800 hover:border-blue-700"
                      }`}
                    >
                      {key}. {currentQuestion[`option_${key.toLowerCase()}`]}
                    </button>
                  ))}
                  <button
                    onClick={handleNext}
                    className="mt-4 w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg transition-colors"
                  >
                    {currentIndex + 1 === questions.length
                      ? "Finish Assessment"
                      : "Next Question"}
                  </button>
                </>
              ) : (
                <p>No questions available. Please seed first.</p>
              )}
            </div>
          )}

          {/* CV/Resume Drop */}
          <div className="mt-6 bg-gray-900 border border-gray-800 rounded-2xl p-6 text-center">
            <p className="text-gray-400 mb-4">
              To access the full assessment and advice, please drop your CV/Resume
            </p>
            <input
              type="file"
              accept=".pdf,.doc,.docx"
              className="border border-gray-700 rounded-lg px-4 py-2 bg-gray-800 text-white"
            />
          </div>
        </div>
      </div>
    </main>
  );
}
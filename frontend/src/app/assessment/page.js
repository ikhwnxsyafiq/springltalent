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
  const [sessionId, setSessionId] = useState(null);

  const [candidates, setCandidates] = useState([]);

  const [selectedBox, setSelectedBox] = useState("Quick Assessment"); // track clicked box

  const [resumeUploaded, setResumeUploaded] = useState(false); // track if resume is uploaded

  const [, setResumeFile] = useState(null); // track resume upload errors
  const [timerLeft, setTimerLeft] = useState(90 * 60); // track time left for current question


  const currentQuestion = questions[currentIndex];

  const progress =
    questions.length > 0
      ? ((currentIndex + 1) / questions.length) * 100
      : 0;

  const handleResumeUpload = (event) => {
    const file = event.target.files[0];
    if (!file) return;
      setResumeFile(file);
      setResumeUploaded(true);

    };

  const loadAssessment = async (type) => {
    try {
      setLoading(true);

      let endpoint = "/api/assessment/quick";
      
      if (type === "Quick Assessment") {

        localStorage.setItem(
          "assessment_type",
          "quick"
        );

        endpoint = "/api/assessment/quick";
      
      } else if (type === "Digital Design") {

        endpoint = "/api/assessment/domain/digital_design";

      } else if (type === "Analog Design") {

        endpoint = "/api/assessment/domain/analog_design";

      } else if (type === "Physical Backend") {
        endpoint = "/api/assessment/domain/backend";
      
      } else if (type === "Mixed-Signal") {
        endpoint = "/api/assessment/domain/mixed_signal";

      } else if (type === "Verification") {
        endpoint = "/api/assessment/domain/verification";

      } else if (type === "EDA Tools") {
        endpoint = "/api/assessment/domain/eda_tools";

      } else if (type === "Full Assessment") {

        localStorage.setItem(
          "assessment_type",
          "full"
        );

        endpoint = "/api/assessment/full";
      }

      const data = await apiRequest(endpoint);

      setQuestions(data.questions || []);
      setCurrentIndex(0);
      setSelectedAnswer("");
      setSelectedBox(type);

    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
 };



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

    if (selectedBox !==  "Full Assessment"){
      return;
    }

    if (timerLeft <= 0) {

      router.push(
        `/results?session_id=${sessionId}`
      );

      return;
    }

    const timer = setInterval(() => {

      setTimerLeft(
        (prev) => prev - 1
      );

    }, 1000);

    return () => clearInterval(timer);

  }, [
    selectedBox,
    timerLeft,
    sessionId,
    router
  ]);
  
  useEffect(() => {
    
    async function initializeAssessment() {
      try {
        const candidateId = localStorage.getItem(
          "candidate_id"
        );
        const session = await apiRequest(
          "/api/assessment/start",
          {
            method: "POST",
            body: JSON.stringify({
              candidate_id: candidateId
            })
          }
        );

        setSessionId(session.session_id);
        
        localStorage.setItem(
          "assessment_type",
          "quick"
        );
        
        const data = await apiRequest(
          "/api/assessment/quick"
        );

        setQuestions(data.questions || []);

        const leaderboard = await apiRequest(
          "/api/leaderboard"
        );
        setCandidates(leaderboard);

      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    }

    initializeAssessment();
  }, []);

  const handleNext = async () => {
    if (!selectedAnswer) {
      setError("Please select an answer before continuing.");
      return;
    }

    setError("");

    try {
      await apiRequest(
        "/api/assessment/answer",
        {
          method: "POST",
          body: JSON.stringify({
            session_id: sessionId,
            question_id: currentQuestion.id,
            selected_answer: selectedAnswer,
          }),
        }
      );
    } catch (error) {
      setError(error.message);
      return;
    }

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
      try {
        await apiRequest(
          `/api/assessment/complete/${sessionId}`,
          {
            method: "POST"
          }
        );
      } catch (error) {
        console.error(error);
      }

      localStorage.setItem(
        "springtalent_answers",
        JSON.stringify(updatedAnswers)
      );

      router.push(
        `/results?session_id=${sessionId}`
      );

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
              key={c.candidate_id}
              className="bg-gray-800 p-3 rounded-lg border border-gray-700"
            >
              <p className="font-semibold">{c.name}</p>
              <p className="text-sm text-gray-400">
                Score: {c.score}%
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
                onClick={() => {
                  
                  if (
                    box === "Full Assessment" &&
                    !resumeUploaded
                  ) {
                    alert(
                      "Please upload your CV/Resume to access the Full Assessment."
                    );
                    return;
                  }

                  loadAssessment(box);


                }}
                  className={`py-4 px-2 rounded-lg font-semibold text-center transition-colors
                  ${
                    selectedBox === box
                      ? "bg-blue-600 text-white"
                      : "bg-gray-800 text-gray-300 hover:bg-gray-700"
                  }`}
              >
                {
                box === "Full Assessment" &&
                !resumeUploaded
                  ? "Full Assessment 🔒"
                  : box
                }
              </button>
            ))}
          </div>

          {/* Question/Test Panel */}
          {selectedBox && (
            <div className="bg-gray-900 border border-gray-800 rounded-2xl p-8">


              {/* Header */}
              <div className="flex justify-between items-center mb-4">

                <h2 className="text-xl font-semibold mb-4">
                  {selectedBox} Question/Test
                </h2>

                {selectedBox === "Full Assessment" && (
                  <div className="bg-red-900 px-4 py-2 rounded-lg">
                    ⏱ {String(
                      Math.floor(timerLeft / 60)
                    ).padStart(2, "0")}
                    :
                    {String(
                      timerLeft % 60
                    ).padStart(2, "0")}
                    
                  </div>
                )}

              </div>

              {/* Progress Bar */}
              <div className="mb-6">

                <div className="flex justify-between text-sm text-gray-400mb-2">

                  <span>
                    Question {currentIndex + 1} of {questions.length}
                  </span>

                  <span>
                    {Math.round(progress)}%
                  </span>

                </div>

                <div className="w-full bg-gray-800 rounded-full h-3">

                  <div 
                    className="bg-cyan-500 h-3 rounded-full transition-all duration-300"
                    style={{
                      width: `${progress}%`
                    }}

                  />
                </div>

              </div>
              
              {/* Question Content*/}
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
                <p>
                  No questions available. Please seed first.
                </p>

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
              onChange={handleResumeUpload}
              className="border border-gray-700 rounded-lg px-4 py-2 bg-gray-800 text-white"
            />

            {resumeUploaded ? (
              <p className="mt-3 text-green-400">
                ✅ Resume uploaded successfully
              </p>
            ) : (
              <p className="mt-3 text-yellow-400">
                ⚠ Upload resume to unlock Full Assessment
              </p>
            )}

          </div>
        </div>
      </div>
    </main>
  );
}
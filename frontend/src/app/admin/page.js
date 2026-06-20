"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { apiRequest } from "@/lib/api";

export default function AdminPage() {

  const router = useRouter();

  const [candidates, setCandidates] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {

    const token = localStorage.getItem(
      "admin_token"
    );

    if (!token) {

      router.push("/admin/login");

      return;
    }

    async function loadCandidates() {

      try {

        const data = await apiRequest(
          "/api/candidate"
        );

        setCandidates(data);

      } catch (error) {

        console.error(error);

      } finally {

        setLoading(false);

      }

    }

    loadCandidates();

  }, [router]);

  function handleLogout() {

    localStorage.removeItem(
      "admin_token"
    );

    router.push(
      "/admin/login"
    );

  }

  if (loading) {
    return (
      <main className="min-h-screen bg-gray-950 text-white flex items-center justify-center">
        Loading candidates...
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-gray-950 text-white p-8">

      <div className="flex justify-between items-center mb-8">

        <h1 className="text-4xl font-bold text-cyan-400">
          Recruiter Dashboard
        </h1>

        <button
          onClick={handleLogout}
          className="bg-red-600 hover:bg-red-700 px-4 py-2 rounded-lg"
        >
          Logout
        </button>

      </div>

      <div className="bg-gray-900 rounded-2xl border border-gray-800 overflow-hidden">

        <table className="w-full">

          <thead className="bg-gray-800">
            <tr>
              <th className="p-4 text-left">
                Name
              </th>

              <th className="p-4 text-left">
                Email
              </th>

              <th className="p-4 text-left">
                University
              </th>

              <th className="p-4 text-left">
                CGPA
              </th>

              <th className="p-4 text-left">
                Actions
              </th>
            </tr>
          </thead>

          <tbody>

            {candidates.map((candidate) => (

              <tr
                key={candidate.id}
                className="border-t border-gray-800"
              >

                <td className="p-4">
                  {candidate.full_name}
                </td>

                <td className="p-4">
                  {candidate.email}
                </td>

                <td className="p-4">
                  {candidate.university}
                </td>

                <td className="p-4">
                  {candidate.cgpa}
                </td>

                <td className="p-4">

                  <a
                    href={`/admin/candidate/${candidate.id}`}
                    className="bg-cyan-600 hover:bg-cyan-700 text-white px-4 py-2 rounded-lg"
                  >
                    View
                  </a>

                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </main>
  );
}
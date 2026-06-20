import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-950 text-white">

      {/* Navbar */}
      <nav className="flex items-center justify-between px-8 py-5 border-b border-gray-800">
        <h1 className="text-xl font-bold">🧑‍💻 SpringTalent</h1>
      </nav>

      {/* Hero Section */}
      <section className="flex flex-col items-center justify-center text-center px-4 py-32">
        <span className="bg-blue-900 text-blue-300 text-xs font-medium px-3 py-1 rounded-full mb-6">
          IC Design Assessment Platform
        </span>
        <h2 className="text-5xl font-bold leading-tight max-w-2xl">
          Discover Your IC Design Potential
        </h2>
        <p className="text-gray-400 mt-6 max-w-xl text-lg leading-relaxed">
          Take a 20-question adaptive assessment across digital design, 
          analog design, physical backend, and mixed-signal domains. 
          Get personalised AI-powered recommendations instantly.
        </p>
        <div className="flex gap-4 mt-10">
          {/* Direct link to assessment, no login/register */}
          <Link href="/candidate">
            <button className="bg-blue-600 hover:bg-blue-700 text-white font-semibold px-8 py-3 rounded-lg transition-colors">
              Start Assessment
            </button>
          </Link>
        </div>
      </section>

      {/* Stats */}
      <section className="border-t border-gray-800 py-16">
        <div className="flex justify-center gap-16 flex-wrap px-8">
          {[
            { number: "200", label: "Question Bank" },
            { number: "20", label: "Questions per Test" },
            { number: "4", label: "IC Design Domains" },
            { number: "100", label: "Pilot Candidates" },
          ].map((stat) => (
            <div key={stat.label} className="text-center">
              <p className="text-4xl font-bold text-blue-400">{stat.number}</p>
              <p className="text-gray-400 mt-1 text-sm">{stat.label}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Features */}
      <section className="py-16 px-8 border-t border-gray-800">
        <h3 className="text-2xl font-bold text-center mb-12">
          What We Assess
        </h3>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 max-w-5xl mx-auto">
          {[
            { icon: "⚡", title: "Digital Design", desc: "RTL, timing analysis, logic synthesis" },
            { icon: "📡", title: "Analog Design", desc: "Circuit theory, amplifiers, filters" },
            { icon: "🔲", title: "Physical Backend", desc: "Floorplanning, routing, signoff" },
            { icon: "🔀", title: "Mixed-Signal", desc: "ADC, DAC, interface design" },
          ].map((feature) => (
            <div key={feature.title} className="bg-gray-900 border border-gray-800 rounded-xl p-6 hover:border-blue-800 transition-colors">
              <span className="text-3xl">{feature.icon}</span>
              <h4 className="font-semibold mt-3 mb-2">{feature.title}</h4>
              <p className="text-gray-400 text-sm">{feature.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-gray-800 py-8 text-center text-gray-500 text-sm">
        © 2026 SpringTalent · Spring Semiconductor Sdn Bhd
      </footer>
    </div>
  );
}
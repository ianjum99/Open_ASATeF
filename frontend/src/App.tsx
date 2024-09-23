import React from 'react';
import Dashboard from './components/Dashboard';
import HumanAICollaboration from './components/HumanAICollaboration';

function App() {
  return (
    <div className="App">
      <header className="bg-gray-800 text-white p-4">
        <h1 className="text-2xl font-bold">AI Stress-Testing Framework</h1>
      </header>
      <main className="container mx-auto p-4">
        <Dashboard />
        <HumanAICollaboration />
      </main>
    </div>
  );
}

export default App;
import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import axios from 'axios';

interface TestResult {
  id: number;
  timestamp: string;
  scenario: {
    type: string;
    content: string;
  };
  responses: {
    [key: string]: string;
  };
  issues: {
    [key: string]: string[];
  };
  human_verification: string;
}

interface SafeguardEffectiveness {
  [key: string]: number;
}

const Dashboard: React.FC = () => {
  const [testResults, setTestResults] = useState<TestResult[]>([]);
  const [safeguardEffectiveness, setSafeguardEffectiveness] = useState<SafeguardEffectiveness>({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [scenarioType, setScenarioType] = useState('');
  const [scenarioContent, setScenarioContent] = useState('');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const resultsResponse = await axios.get<TestResult[]>('http://localhost:8000/api/test-results');
      const effectivenessResponse = await axios.get<SafeguardEffectiveness>('http://localhost:8000/api/safeguard-effectiveness');
      setTestResults(resultsResponse.data);
      setSafeguardEffectiveness(effectivenessResponse.data);
      setError(null);
    } catch (error) {
      console.error('Error fetching data:', error);
      setError('Failed to fetch data. Please try again later.');
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await axios.post('http://localhost:8000/api/run-test', {
        scenario_type: scenarioType,
        content: scenarioContent
      });
      setScenarioType('');
      setScenarioContent('');
      alert('Test started successfully. Results will appear soon.');
      // Fetch updated results after a short delay
      setTimeout(fetchData, 5000);
    } catch (error) {
      console.error('Error running test:', error);
      setError('Failed to run test. Please try again later.');
    }
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="dashboard p-6">
      <h2 className="text-2xl font-bold mb-4">Dashboard</h2>
      
      <div className="mb-8">
        <h3 className="text-xl font-semibold mb-2">Run New Test</h3>
        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="scenarioType" className="block text-sm font-medium text-gray-700">Scenario Type</label>
            <input
              type="text"
              id="scenarioType"
              value={scenarioType}
              onChange={(e) => setScenarioType(e.target.value)}
              className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2"
              required
            />
          </div>
          <div>
            <label htmlFor="scenarioContent" className="block text-sm font-medium text-gray-700">Scenario Content</label>
            <textarea
              id="scenarioContent"
              value={scenarioContent}
              onChange={(e) => setScenarioContent(e.target.value)}
              className="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2"
              rows={4}
              required
            ></textarea>
          </div>
          <button type="submit" className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
            Run Test
          </button>
        </form>
      </div>
      
      <div className="mb-8">
        <h3 className="text-xl font-semibold mb-2">Safeguard Effectiveness</h3>
        <ResponsiveContainer width="100%" height={300}>
          <BarChart data={Object.entries(safeguardEffectiveness).map(([name, score]) => ({ name, score }))}>
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis dataKey="name" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="score" fill="#8884d8" />
          </BarChart>
        </ResponsiveContainer>
      </div>
      
      <div>
        <h3 className="text-xl font-semibold mb-2">Recent Test Results</h3>
        <table className="min-w-full bg-white">
          <thead>
            <tr>
              <th className="px-4 py-2">Timestamp</th>
              <th className="px-4 py-2">Scenario</th>
              <th className="px-4 py-2">Issues</th>
              <th className="px-4 py-2">Human Verification</th>
            </tr>
          </thead>
          <tbody>
            {testResults.map((result) => (
              <tr key={result.id}>
                <td className="border px-4 py-2">{new Date(result.timestamp).toLocaleString()}</td>
                <td className="border px-4 py-2">{result.scenario.content}</td>
                <td className="border px-4 py-2">
                  {Object.entries(result.issues).map(([model, issues]) => (
                    <div key={model}>
                      <strong>{model}:</strong> {issues.join(', ')}
                    </div>
                  ))}
                </td>
                <td className="border px-4 py-2">{result.human_verification}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Dashboard;

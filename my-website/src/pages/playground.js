import React, { useState } from 'react';
import Layout from '@theme/Layout';
// Import your JS interpreter
import { runVarlang } from '../interpreter';

export default function Playground() {
  const [code, setCode] = useState('');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleRun = async () => {
    setLoading(true);
    setOutput('');
    try {
      // Run the interpreter directly in the browser
      const result = runVarlang(code);
      setOutput(result);
    } catch (err) {
      setOutput('Error: ' + err.message);
    }
    setLoading(false);
  };

  return (
    <Layout title="Playground" description="Try the 6ix Esolang interpreter in your browser!">
      <div style={{ maxWidth: 700, margin: '2rem auto', padding: '1rem' }}>
        <h1>6ix Esolang Playground</h1>
        <textarea
          value={code}
          onChange={e => setCode(e.target.value)}
          rows={10}
          style={{ width: '100%', fontFamily: 'monospace', fontSize: 16, marginBottom: 12 }}
          placeholder='Type your 6ix Esolang code here...'
        />
        <div>
          <button onClick={handleRun} disabled={loading} style={{ padding: '0.5rem 1.5rem', fontSize: 16 }}>
            {loading ? 'Running...' : 'Run'}
          </button>
        </div>
        <div style={{ marginTop: 24 }}>
          <h3>Output:</h3>
          <pre style={{ background: '#222', color: '#fff', padding: 16, minHeight: 60 }}>
            {output}
          </pre>
        </div>
      </div>
    </Layout>
  );
}
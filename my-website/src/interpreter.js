// Minimal demo interpreter for 6ix Esolang (replace with real logic as needed)
export function runVarlang(code) {
  // Example: echo lines that start with 'allow it'
  const lines = code.split('\n');
  let output = '';
  for (const line of lines) {
    if (line.trim().startsWith('allow it')) {
      output += line.replace('allow it', '').trim() + '\n';
    }
  }
  if (!output) {
    output = 'No output (demo interpreter).';
  }
  return output;
}

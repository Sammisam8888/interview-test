// Converted utilities from analysis.py to JavaScript for use in Next.js
export function calculateSalary(hours, rate) {
  const total = hours * rate;
  const bonus = 500;
  return total + bonus;
}

export function processData(data) {
  const cleaned = data.map((d) => String(d).trim().toLowerCase());
  const unique = Array.from(new Set(cleaned));
  return unique;
}

export function generateReport(name, score) {
  const grade = score > 90 ? 'A' : 'B';
  return `Student: ${name}, Grade: ${grade}`;
}

export function displaySummary(data) {
  console.log('Summary Report:');
  data.forEach((item) => console.log(`- ${item}`));
}

import "./styles/Career.css";
import { config } from "../config";

const getDisplayYear = (period: string) => {
  if (period.includes("Present") || period.includes("NOW")) return "NOW";
  if (period.includes(" - ")) return period.split(" - ")[0].split(" ").pop(); // Extract year
  if (period.includes(" – ")) return period.split(" – ")[0].split(" ").pop(); // Handle en-dash
  return period;
};

const Career = () => {
  return (
    <div className="career-section section-container">
      <div className="career-container">
        <h2>
          My career <span>&</span>
          <br /> experience
        </h2>
        <div className="career-info">
          <div className="career-timeline">
            <div className="career-dot"></div>
          </div>
          {config.experiences.map((exp, index) => (
            <div key={index} className="career-info-box">
              <div className="career-info-in">
                <div className="career-role">
                  <h4>{exp.position}</h4>
                  <h5>{exp.company}</h5>
                </div>
                <h3>{getDisplayYear(exp.period)}</h3>
              </div>
              <div className="career-details">
                <p style={{ marginBottom: '15px' }}>{exp.description}</p>
                {exp.responsibilities && (
                  <ul style={{ paddingLeft: '20px', margin: 0 }}>
                    {exp.responsibilities.map((resp, i) => (
                      <li key={i} style={{ fontSize: '13px', fontWeight: 300, lineHeight: '20px', marginBottom: '8px', opacity: 0.8 }}>
                        {resp}
                      </li>
                    ))}
                  </ul>
                )}
                <div style={{ fontSize: '12px', marginTop: '15px', color: 'var(--accentColor)', opacity: 0.9 }}>
                  {exp.period}
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Career;

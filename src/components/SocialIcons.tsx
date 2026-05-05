import {
  FaGithub,
  FaInstagram,
  FaLinkedinIn,
  FaXTwitter,
} from "react-icons/fa6";
import "./styles/SocialIcons.css";
import { TbNotes } from "react-icons/tb";
import { useEffect } from "react";
import HoverLinks from "./HoverLinks";
import { config } from "../config";

const SocialIcons = () => {
  useEffect(() => {
    const social = document.getElementById("social") as HTMLElement;
    if (!social) return;

    // Fix: store cleanup functions per listener and use correct rect on mousemove
    const cleanupFns: (() => void)[] = [];

    social.querySelectorAll("span").forEach((item) => {
      const elem = item as HTMLElement;
      const link = elem.querySelector("a") as HTMLElement;
      if (!link) return;

      let mouseX = elem.offsetWidth / 2;
      let mouseY = elem.offsetHeight / 2;
      let currentX = 0;
      let currentY = 0;
      let rafId: number;

      const updatePosition = () => {
        currentX += (mouseX - currentX) * 0.1;
        currentY += (mouseY - currentY) * 0.1;
        link.style.setProperty("--siLeft", `${currentX}px`);
        link.style.setProperty("--siTop", `${currentY}px`);
        rafId = requestAnimationFrame(updatePosition);
      };
      rafId = requestAnimationFrame(updatePosition);

      // Fix: use elem (not document) for mousemove to get accurate coords
      const onMouseMove = (e: MouseEvent) => {
        const rect = elem.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        if (x < 40 && x > 10 && y < 40 && y > 5) {
          mouseX = x;
          mouseY = y;
        } else {
          mouseX = elem.offsetWidth / 2;
          mouseY = elem.offsetHeight / 2;
        }
      };

      // Fix: listen on elem instead of document
      elem.addEventListener("mousemove", onMouseMove);

      cleanupFns.push(() => {
        elem.removeEventListener("mousemove", onMouseMove);
        cancelAnimationFrame(rafId);
      });
    });

    return () => {
      cleanupFns.forEach((fn) => fn());
    };
  }, []);

  return (
    <div className="icons-section">
      <div className="social-icons" data-cursor="icons" id="social">
        <span>
          <a href={config.contact.github} target="_blank" rel="noopener noreferrer">
            <FaGithub />
          </a>
        </span>
        <span>
          <a href={config.contact.linkedin} target="_blank" rel="noopener noreferrer">
            <FaLinkedinIn />
          </a>
        </span>
        {/* Only show Twitter if it's a real account */}
        {config.contact.twitter && config.contact.twitter !== "https://x.com/" && (
          <span>
            <a href={config.contact.twitter} target="_blank" rel="noopener noreferrer">
              <FaXTwitter />
            </a>
          </span>
        )}
        {/* Only show Instagram if it's a real account */}
        {config.contact.instagram && config.contact.instagram !== "https://instagram.com/" && (
          <span>
            <a href={config.contact.instagram} target="_blank" rel="noopener noreferrer">
              <FaInstagram />
            </a>
          </span>
        )}
      </div>
      <a className="resume-button" href="/Resume.pdf" target="_blank" rel="noopener noreferrer">
        <HoverLinks text="RESUME" />
        <span>
          <TbNotes />
        </span>
      </a>
    </div>
  );
};

export default SocialIcons;

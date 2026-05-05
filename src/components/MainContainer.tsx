import { PropsWithChildren, useEffect, useRef, useState } from "react";
import About from "./About";
import Career from "./Career";
import Contact from "./Contact";
import Cursor from "./Cursor";
import Landing from "./Landing";
import Navbar from "./Navbar";
import SocialIcons from "./SocialIcons";
import WhatIDo from "./WhatIDo";
import Work from "./Work";
import TechStackNew from "./TechStackNew";
import CallToAction from "./CallToAction";
import setSplitText from "./utils/splitText";

const MainContainer = ({ children }: PropsWithChildren) => {
  const [isDesktopView, setIsDesktopView] = useState<boolean>(
    window.innerWidth > 1024
  );
  // Fix: isMobile should also update on resize; store it in a ref for the handler
  const isMobileRef = useRef<boolean>(window.innerWidth <= 768);
  const [isMobile, setIsMobile] = useState<boolean>(window.innerWidth <= 768);

  useEffect(() => {
    // Fix: useEffect should have empty deps — the handler reads current window
    // values so it doesn't need to depend on state. This prevents re-registering
    // the listener on every resize crossing the 1024px boundary.
    const resizeHandler = () => {
      setSplitText();
      const desktop = window.innerWidth > 1024;
      const mobile = window.innerWidth <= 768;
      setIsDesktopView(desktop);
      setIsMobile(mobile);
      isMobileRef.current = mobile;
    };
    resizeHandler();
    window.addEventListener("resize", resizeHandler);
    return () => {
      window.removeEventListener("resize", resizeHandler);
    };
  }, []); // Fix: empty deps — single registration, no re-registering

  return (
    <div className="container-main">
      <Cursor />
      <Navbar />
      <SocialIcons />
      {isDesktopView && !isMobile && children}
      <div className="container-main">
        <Landing />
        <About />
        <WhatIDo />
        <Career />
        <Work />
        <TechStackNew />
        <CallToAction />
        <Contact />
      </div>
    </div>
  );
};

export default MainContainer;

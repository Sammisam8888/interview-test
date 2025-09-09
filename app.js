function getProfile() {
    return {
        id: 1,
        name: "Alice Johnson",
        role: "Frontend Engineer",
        skills: [
            "React",
            "Redux",
            "JavaScript",
            "CSS",
            "HTML",
            "TypeScript",
            "Node.js",
            "Webpack",
            "Babel",
            "Testing Library"
        ],
        experience: [
            {
                company: "TechCorp",
                years: 2,
                projects: ["UI Redesign", "Admin Dashboard", "Internal Tools"]
            },
            {
                company: "WebSolutions",
                years: 3,
                projects: ["E-Commerce", "Landing Pages", "CMS Migration"]
            }
        ],
        hobbies: ["Reading", "Gaming", "Traveling", "Photography"]
    };
}

console.log("MAIN BRANCH: Loaded Alice’s Profile");

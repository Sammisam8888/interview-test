function getProfile() {
    return {
        id: 101,
        name: "Bob Smith",
        role: "Mobile App Developer",
        skills: [
            "React Native",
            "Expo",
            "Android",
            "iOS",
            "GraphQL",
            "REST APIs",
            "Firebase",
            "CI/CD",
            "Jest",
            "Detox"
        ],
        experience: [
            {
                company: "AppMakers",
                years: 4,
                projects: ["Social Media App", "Food Delivery App", "Fitness Tracker"]
            },
            {
                company: "StartUpX",
                years: 2,
                projects: ["MVP Development", "Hybrid Mobile Apps"]
            }
        ],
        hobbies: ["Cycling", "Cooking", "Music Production", "Volunteering"]
    };
}

console.log("FEATURE BRANCH: Loaded Bob’s Profile");

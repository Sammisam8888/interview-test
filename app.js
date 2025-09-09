function getProfile() {
    return {
        id: 101,
        name: "Bob",
        role: "Mobile Developer",
        skills: ["React Native", "GraphQL", "Firebase", "CI/CD"],
        hobbies: ["Cycling", "Music", "Cooking"],
        status: "Inactive"
    };
}

function getAddress() {
    return {
        city: "Berlin",
        country: "Germany",
        zip: "10115"
    };
}

function getProjects() {
    return ["Food Delivery App", "Fitness Tracker", "Social Media Platform"];
}

function getPreferences() {
    return {
        theme: "dark",
        language: "German",
        notifications: false
    };
}

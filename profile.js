function getProfile() {
    return {
        id: 1,
        name: "Alice",
        role: "Frontend Engineer",
        skills: ["React", "Redux", "JavaScript", "CSS"],
        hobbies: ["Reading", "Gaming", "Traveling"],
        status: "Active"
    };
}

function getAddress() {
    return {
        city: "New York",
        country: "USA",
        zip: "10001"
    };
}

function getProjects() {
    return ["UI Redesign", "Admin Dashboard", "CMS Migration"];
}

function getPreferences() {
    return {
        theme: "light",
        language: "English",
        notifications: true
    };
}

module.exports = {
    getProfile,
    getAddress,
    getProjects,
    getPreferences
};
import { getAddress, getPreferences, getProfile, getProjects } from '../../profile';

export default function handler(req, res) {
  const payload = {
    profile: getProfile(),
    address: getAddress(),
    projects: getProjects(),
    preferences: getPreferences(),
  };

  res.status(200).json(payload);
}

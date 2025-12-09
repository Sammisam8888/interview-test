import { getAddress, getPreferences, getProfile, getProjects } from '../profile';

export default function Home() {
  const profile = getProfile();
  const address = getAddress();
  const projects = getProjects();
  const prefs = getPreferences();

  return (
    <main style={{fontFamily: 'Arial, sans-serif', padding: 24}}>
      <h1>Profile</h1>
      <section>
        <h2>{profile.name} — {profile.role}</h2>
        <p>Status: {profile.status}</p>
        <p>Location: {address.city}, {address.country} {address.zip}</p>
      </section>

      <section>
        <h3>Skills</h3>
        <ul>
          {profile.skills.map((s) => <li key={s}>{s}</li>)}
        </ul>
      </section>

      <section>
        <h3>Projects</h3>
        <ul>
          {projects.map((p) => <li key={p}>{p}</li>)}
        </ul>
      </section>

      <section>
        <h3>Preferences</h3>
        <pre>{JSON.stringify(prefs, null, 2)}</pre>
      </section>

      <section>
        <h3>API Demo</h3>
        <p>Open <code>/api/profile</code> to fetch the same data as JSON.</p>
      </section>
    </main>
  );
}

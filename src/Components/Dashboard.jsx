import Aside from "./Aside";
import Header from "./Header";
import Main from "./Main";

function Dashboard() {
  return (
    <div className="container flex h-full mx-auto bg-neutral-50 rounded-lg overflow-hidden">
      <Aside />
      <div className="flex-1 flex flex-col overflow-hidden">
        <Header />
        <Main />
      </div>
    </div>
  );
}

export default Dashboard;

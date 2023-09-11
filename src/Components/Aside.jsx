import { useState } from "react";
import { FaLocationArrow } from "react-icons/fa";
import { RiArrowDropDownLine } from "react-icons/ri";
import { MdOutlineInventory2, MdPendingActions } from "react-icons/md";
import { CiSquareQuestion } from "react-icons/ci";

/************* dashboad aside component **********/
export default function Aside() {
  /************* menu list **********/
  const [selectMenu, setSelectMenu] = useState(null);

  const menuList = [
    {
      id: 0,
      text: "Inventory",
      icon: <MdOutlineInventory2 className=" mr-2 " />,
    },
    {
      id: 1,
      text: "Resquest Loadout",
      icon: <CiSquareQuestion className=" mr-2 " />,
    },
    {
      id: 2,
      text: "Pending Loadout",
      icon: <MdPendingActions className=" mr-2 " />,
    },
  ];

  const toggleMenu = (menuId) => {
    selectMenu === menuId ? null : setSelectMenu(menuId);
    menuId === 0 && showLocation();
    menuId === 0 && toggleMargin();
    console.log(menuId);
  };

  /************* function to display and hide locations **********/
  const [showLocations, setShowLocations] = useState(false);

  const showLocation = () => {
    setShowLocations(!showLocations);
  };

  /************* dropdown function **********/
  const [changeMargin, setChangeMargin] = useState(false);

  const toggleMargin = () => {
    setChangeMargin(!changeMargin);
  };

  /************* locations to be fetched from a database **********/
  const locations = ["Warehouse", "Rig-1", "Rig-2", "Rig-3"];

  return (
    <aside className="bg-blue-950 text-white py-4 pr-4 w-64 relative ">
      <div className="text-2xl font-semibold mt-4 mb-14 px-4 ">CementBond</div>

      {menuList.map((menu, index) => (
        <div
          className={`flex locations mt-2 items-center rounded-full rounded-l-none space-x-16  pr-4 pl-4 cursor-pointer hover:pr-6 transition-all duration-300 ease-in-out ${
            menu.id === selectMenu
              ? "bg-white text-blue-950"
              : "bg-blue-950 text-white"
          } ${index === 0 && changeMargin && "mb-32"}`}
          key={menu.id}
          onClick={() => toggleMenu(menu.id)}
        >
          <p className="p-2 inline-flex items-center text-md">
            {menu.icon}
            {menu.text}
          </p>
          {index === 0 && <RiArrowDropDownLine className="text-2xl" />}
        </div>
      ))}
      <div className="ml-10 py-2 absolute top-40 transition-all duration-300 ease-in-out">
        {showLocations && (
          <ul>
            {locations.map((location, index) => (
              <li className="mb-2" key={index}>
                <a
                  href="#"
                  className="px-4 py-2 text-gray-300 hover:text-white"
                >
                  {location}
                </a>
              </li>
            ))}
          </ul>
        )}
      </div>
    </aside>
  );
}

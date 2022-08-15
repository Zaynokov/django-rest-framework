import React from "react";
import { Link } from "react-router-dom";

const Menu = () => {
    return (
        <nav>
            <ul>
              <li>
                <Link to='users'>Users</Link>
              </li>
              <li>
                <Link to='projects'>Projects</Link>
              </li>
              <li>
                <Link to='notes'>Notes</Link>
              </li>
            </ul>
          </nav>
    )
}

export default Menu
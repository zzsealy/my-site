import React from "react"
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap';
import login from "../Admin/login"


class Nav extends React.Component{
    render() {
        return(
        <div>
            <div class="sidebar-menu toggle-others fixed">
                <div class="sidebar-menu-inner">
                    <header class="logo-env">
                        <div class="logo">
                            <a href="index.html" class="logo-expanded">
                                <img src="../assets/images/logo@2x.png" width="100%" alt="" />
                            </a>
                            <a href="index.html" class="logo-collapsed">
                                <img src="../assets/images/logo-collapsed@2x.png" width="40" alt="" />
                            </a>
                        </div>
                        <div class="mobile-menu-toggle visible-xs">
                            
                        </div>
                    </header>
                    <ul id="main-menu" class="main-menu">
                        <li>
                            <a href="#常用推荐" class="smooth">
                                <i class="linecons-star"></i>
                                <span class="title">常用推荐</span>
                            </a>
                        </li>
                        
                    </ul>
                    </div>
                
            </div>
        </div>
        )
    }
}


export default Nav
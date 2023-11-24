import { useSelector } from "react-redux";
import NotAuthenticatedLayout from "./layouts/NotAuthenticatedLayout";
import AuthenticatedLayout from "./layouts/AuthenticatedLayout";
import DrawerLayout from "./layouts/DrawerLayout";

import LoginPage from "./features/login/LoginPage";
import DashboardPage from "./features/dashboard/DashboardPage";
import CoursePage from "./features/course/CoursePage";

const { createBrowserRouter, RouterProvider } = require("react-router-dom");

function UrlPaths() {
    const { access } = useSelector((state) => state.auth);

    const routesForAuthenticatedOnly = [
        {
            path: "/",
            element: <AuthenticatedLayout />,
            children: [
                {
                    path: "/",
                    element: <DrawerLayout />,
                    children: [
                        {
                            path: "",
                            element: <DashboardPage />
                        }
                    ]
                },
                {
                    path: ":course",
                    element: <CoursePage />,
                    // children: [
                    //     {
                    //         path: ":meeting",
                    //         element: <MeetingPage />
                    //     }
                    // ]
                }
            ]
        }
    ];

    const routesForNotAuthenticatedOnly = [
        {
            path: "/",
            element: <NotAuthenticatedLayout />,
            children: [
                {
                    path: "",
                    element: <LoginPage />
                }
            ]
        }
    ];

    const router = createBrowserRouter([
        ...(!access ? routesForNotAuthenticatedOnly : []),
        ...routesForAuthenticatedOnly
    ]);

    return <RouterProvider router={router} />;
}

export default UrlPaths;
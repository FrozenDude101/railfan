import { StrictMode } from 'react';
import ReactDOM from 'react-dom/client';
import { RouterProvider, createRouter } from '@tanstack/react-router';
import reportWebVitals from './reportWebVitals';
import { routeTree } from './routeTree.gen';
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from '@tanstack/react-query-devtools';

import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

declare module '@tanstack/react-router' {
    interface Register {
            router: typeof router
    }
}

const router = createRouter({
    routeTree,
    context: {},
    defaultPreload: 'intent',
    scrollRestoration: true,
    defaultStructuralSharing: true,
    defaultPreloadStaleTime: 0,
});

const rootElement = document.getElementById('app');

if (rootElement && !rootElement.innerHTML) {
    const root = ReactDOM.createRoot(rootElement)
    root.render(
        <StrictMode>
            <QueryClientProvider client={ new QueryClient() }>
                <RouterProvider router={ router }/>
                <ReactQueryDevtools buttonPosition="bottom-right"/>
            </QueryClientProvider>
        </StrictMode>,
    );
}

reportWebVitals(console.log);

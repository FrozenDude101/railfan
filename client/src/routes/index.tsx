import createFetchClient from "openapi-fetch";
import createClient from "openapi-react-query";
import { createFileRoute } from '@tanstack/react-router';
import type { paths } from "../lib/api";


export const Route = createFileRoute('/')({
    component: App,
});

const fetchClient = createFetchClient<paths>({
    baseUrl: "http://localhost:8000",
});
const api = createClient(fetchClient);

function App() {

    const { data, isLoading } = api.useQuery("get", "/users/");

    if (isLoading) {
        return "Loading";
    }

    return (
        <div>
            { data?.length }
        </div>
    );
}

from anticaptchaofficial.recaptchav2proxyless import *

def g_response():
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key("cda594b619433a2b0d5a04971da967bf")
    solver.set_website_url("https://rendezvousparis.hermes.com/client/register")
    solver.set_website_key("6LdUViwUAAAAAOBJjtMsmKc9C7200Djd31w2mCs7")
    return solver.solve_and_return_solution()
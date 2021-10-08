from anticaptchaofficial.recaptchav3proxyless import *

def g_response():
    solver = recaptchaV3Proxyless()
    solver.set_verbose(1)
    solver.set_key("cda594b619433a2b0d5a04971da967bf")
    solver.set_website_url("https://rendezvousparis.hermes.com/client/register")
    solver.set_website_key("6LdguR8cAAAAAI8aBz88G9v3x-eaqpqBpAe14aH6")
    solver.set_page_action("registion")
    return solver.solve_and_return_solution()
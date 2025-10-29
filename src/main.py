import flet as ft
import random

def main(page: ft.Page):
    def reroll_job(job_slot):
        jobs = []
        if (freelancer_check.value):
            jobs += job_freelancer
        if (wind_jobs_check.value):
            jobs += wind_jobs
        if (water_jobs_check.value):
            jobs += water_jobs
        if (fire_jobs_check.value):
            jobs += fire_jobs
        if (earth_jobs_check.value):
            jobs += earth_jobs
        if (mime_check.value):
            jobs += job_mime
        if (advance_jobs_check.value):
            jobs += advance_jobs
        if len(jobs) > 0:
            match job_slot:
                case 1:
                    output_job_one.value = random.choice(jobs)
                case 2:
                    output_job_two.value = random.choice(jobs)
                case 3:
                    output_job_three.value = random.choice(jobs)
                case 4:
                    output_job_four.value = random.choice(jobs)
                case _:
                    #by default reroll all jobs
                    random_jobs = []
                    all_jobs = []
                    for i in range(1, int(options_max_duplicates.value) + 1):
                        all_jobs += jobs
                    for i in range(0, 4):
                        random_job = random.choice(all_jobs)
                        all_jobs.remove(random_job)
                        random_jobs.append(random_job)
                    output_job_one.value = random_jobs[0]
                    output_job_two.value = random_jobs[1]
                    output_job_three.value = random_jobs[2]
                    output_job_four.value = random_jobs[3]
            page.update()
    def reroll_all(e):
        reroll_job(5)
    def reroll_job_one(e):
        reroll_job(1)
    def reroll_job_two(e):
        reroll_job(2)
    def reroll_job_three(e):
        reroll_job(3)
    def reroll_job_four(e):
        reroll_job(4)
    page.title = "Final Fantasy V Job Randomizer"
    job_freelancer = ["Freelancer"]
    wind_jobs = ["Knight", "Monk", "Thief", "Black Mage", "White Mage", "Blue Mage"]
    water_jobs = ["Red Mage", "Time Mage", "Summoner", "Berserker", "Mystic Knight"]
    fire_jobs = ["Beastmaster", "Geomancer", "Ninja", "Ranger", "Bard"]
    earth_jobs = ["Dragoon", "Dancer", "Samurai", "Chemist"]
    job_mime = ["Mime"]
    advance_jobs = ["Necromancer", "Canoneer", "Gladiator", "Oracle"]

    freelancer_check = ft.Checkbox(label="Freelancer", value=False)
    wind_jobs_check = ft.Checkbox(label="Wind Crystal Jobs", value=False)
    water_jobs_check = ft.Checkbox(label="Water Crystal Jobs", value=False)
    fire_jobs_check = ft.Checkbox(label="Fire Crystal Jobs", value=False)
    earth_jobs_check = ft.Checkbox(label="Earth Crystal Jobs", value=False)
    mime_check = ft.Checkbox(label="Mime", value=False)
    advance_jobs_check = ft.Checkbox(label="Advance Jobs", value=False)

    rule_assign_check = ft.Checkbox(label="Assign to character", value=False)
    rule_four_job_fiesta_check = ft.Checkbox(label="Four Job Fiesta", value=False)

    reroll_all_button = ft.Button("Reroll all jobs", on_click=reroll_all)
    reroll_job_one_button = ft.Button("Reroll first job", on_click=reroll_job_one)
    reroll_job_two_button = ft.Button("Reroll second job", on_click=reroll_job_two)
    reroll_job_three_button = ft.Button("Reroll third job", on_click=reroll_job_three)
    reroll_job_four_button = ft.Button("Reroll fourth job", on_click=reroll_job_four)

    options_max_duplicates = ft.TextField("1", width=100)

    output_job_one = ft.TextField(label="Job one", width=200, read_only=True)
    output_job_two = ft.TextField(label="Job two", width=200, read_only=True)
    output_job_three = ft.TextField(label="Job three", width=200, read_only=True)
    output_job_four = ft.TextField(label="Job four", width=200, read_only=True)

    page.add(
        ft.Row([
            ft.Column([ft.Text("Jobs available:"),
                    freelancer_check,
                    wind_jobs_check,
                    water_jobs_check,
                    fire_jobs_check,
                    earth_jobs_check,
                    mime_check,
                    advance_jobs_check,
                    ], alignment=ft.MainAxisAlignment.START),
            ft.Column([ft.Text("Rules selected:"),
                    rule_assign_check,
                    rule_four_job_fiesta_check,
                    ], alignment=ft.MainAxisAlignment.START), 
            ft.Column([ft.Text("Options:"),
                    ft.Row([ft.Text("Max duplicates: "), options_max_duplicates]),
                    ], alignment=ft.MainAxisAlignment.START),
            ft.Column([reroll_all_button,
                    reroll_job_one_button,
                    reroll_job_two_button,
                    reroll_job_three_button,
                    reroll_job_four_button,
                    ], alignment=ft.MainAxisAlignment.START),                
                    ], alignment=ft.MainAxisAlignment.START),
        ft.Row([
            output_job_one,
            output_job_two,
            output_job_three,
            output_job_four,
        ],)
    )


ft.app(main)

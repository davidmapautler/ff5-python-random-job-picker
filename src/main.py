import flet as ft
import random

def main(page: ft.Page):
    def reroll_job(job_slot):
        if (not rule_four_job_fiesta_check.value):
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
                output_info_text.value = ""
                page.update()
            else:
                output_info_text.value = "Please select one or more job sets from the left-most group of checkboxes"
                page.update()
        else:
            match job_slot:
                case 1:
                    output_job_one.value = random.choice(wind_jobs)
                case 2:
                    output_job_two.value = random.choice(water_jobs)
                case 3:
                    output_job_three.value = random.choice(fire_jobs)
                case 4:
                    output_job_four.value = random.choice(earth_jobs)
                case _:
                    output_job_one.value = random.choice(wind_jobs)
                    output_job_two.value = random.choice(water_jobs)
                    output_job_three.value = random.choice(fire_jobs)
                    output_job_four.value = random.choice(earth_jobs)
            page.update()
    def default_job_labels():
        output_job_one.label = "Job one"
        output_job_two.label = "Job two"
        output_job_three.label = "Job three"
        output_job_four.label = "Job four"
        reroll_job_one_button.text = "Reroll first job"
        reroll_job_two_button.text = "Reroll second job"
        reroll_job_three_button.text = "Reroll third job"
        reroll_job_four_button.text = "Reroll fourth job"
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
    def rule_assign(e):
        if (rule_assign_check.value):
            output_job_one.label = "Bartz's Job"
            output_job_two.label = "Lenna's Job"
            output_job_three.label = "Galuf/Krile's Job"
            output_job_four.label = "Faris's Job"
            reroll_job_one_button.text = "Reroll Bartz's job"
            reroll_job_two_button.text = "Reroll Lenna's job"
            reroll_job_three_button.text = "Reroll Galuf/Krile's job"
            reroll_job_four_button.text = "Reroll Faris's job"
        else:
            default_job_labels()
        rule_four_job_fiesta_check.value = False
        page.update()
    def rule_four_job_fiesta(e):
        if (rule_four_job_fiesta_check.value):
            output_job_one.label = "Wind Job"
            output_job_two.label = "Water Job"
            output_job_three.label = "Fire Job"
            output_job_four.label = "Earth Job"
            reroll_job_one_button.text = "Reroll wind job"
            reroll_job_two_button.text = "Reroll water job"
            reroll_job_three_button.text = "Reroll fire job"
            reroll_job_four_button.text = "Reroll earth job"
            output_info_text.value = "Note that four job fiesta ignores checked jobs in the left-most column and will assign jobs based on the rules of the popular four job fiesta ruleset."
        else:
            default_job_labels()
            output_info_text.value = ""
        rule_assign_check.value = False
        page.update()
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

    #TODO: Change these to radios since they're exclusive
    rule_assign_check = ft.Checkbox(label="Assign to character", value=False, on_change=rule_assign)
    rule_four_job_fiesta_check = ft.Checkbox(label="Four Job Fiesta", value=False, on_change=rule_four_job_fiesta)

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

    output_info_text = ft.Text("")

    page.add(
        ft.Row([
            #TODO: Figure out why vertical alignment isn't working
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
        ]),
        ft.Row([
            output_info_text,
        ]),
    )


ft.app(main)

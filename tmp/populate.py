# region				-----External Imports-----
import development
import decimal
import django
# endregion


#? This script needs to test performance of Django admin
#? and find database query leaks
def main():
    projects = []

    for idx in range(1, 20):
        projects.append(
            development.models.Project(
                current_status="active_development",
                sale_status="qualified_to_buy",
                title=f"Project #{idx}"
            )
        )

    development.models.Project.objects\
        .bulk_create(projects)
        
    projects = development.models.Project\
        .objects.all()
    
    for ida, project in enumerate(projects, 1):
        print(f"{project}")

        for idb in range(1, 4):
            stage = development.models.Stage.objects.create(
                title=f"Stage #{ida}.{idb}",
                project=project
            )

            print(f"\t{stage}")

            for idc in range(1, 4):
                feature = development.models.Feature.objects.create(
                    start_date=django.utils.timezone.now(),
                    title=f"Feature #{ida}.{idb}.{idc}",
                    priority="high",
                    stage=stage
                )

                print(f"\t\t{feature}")

                for idd in range(1, 4):
                    task = development.models.Task.objects.create(
                        title=f"Task #{ida}.{idb}.{idc}.{idd}",
                        start_date=django.utils.timezone.now(),
                        development_hour=decimal.Decimal(10),
                        rate=decimal.Decimal(40.00),
                        status="completed",
                        qa_status="passed",
                        feature=feature
                    )

                    print(f"\t\t\t{task}")

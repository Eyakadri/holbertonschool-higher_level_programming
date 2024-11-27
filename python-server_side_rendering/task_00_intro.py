import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def generate_invitations(template: str, attendees: list) -> None:
    """
    Generate personalized invitation files from a template and list of attendees.
    
    Args:
        template (str): The invitation template with placeholders
        attendees (list): List of dictionaries containing attendee information
    """
    if not isinstance(template, str):
        logger.error(f"Template must be a string, got {type(template)}")
        return
        
    if not isinstance(attendees, list):
        logger.error(f"Attendees must be a list, got {type(attendees)}")
        return
        
    if not template.strip():
        logger.error("Template is empty, no output files generated.")
        return
        
    if not attendees:
        logger.error("No data provided, no output files generated.")
        return
        

    for index, attendee in enumerate(attendees, 1):
        if not isinstance(attendee, dict):
            logger.error(f"Attendee data must be a dictionary, got {type(attendee)}")
            continue
            

        invitation = template
        for field in ['name', 'event_title', 'event_date', 'event_location']:
            value = attendee.get(field, 'N/A')
            if value is None:
                value = 'N/A'
            invitation = invitation.replace(f"{{{field}}}", str(value))
            
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as file:
                file.write(invitation)
            logger.info(f"Generated invitation for {attendee.get('name', 'Unknown')} - {output_filename}")
        except IOError as e:
            logger.error(f"Error writing file {output_filename}: {str(e)}")
        except Exception as e:
            logger.error(f"Unexpected error processing attendee {index}: {str(e)}")
